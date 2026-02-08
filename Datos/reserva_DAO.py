#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia


from datetime import datetime
from Datos.conexion import Conexion
from Dominio.reserva import Reserva
import pyodbc as bd


class ReservaDAO:
    # Consultas SQL
    _INSERT = ("INSERT INTO Reserva (IDReserva, IDHuesped, IDHabitacion, FechaIngreso, FechaSalida,"
               "NumeroNoches, EstadoReserva)"
               "VALUES (?, ?, ?, ?, ?, ?, ?)")

    _UPDATE = ("UPDATE Reserva SET IDHuesped=?, IDHabitacion=?, FechaIngreso=?, FechaSalida=?, NumeroNoches=?, EstadoReserva=?"
               " WHERE IDReserva=?")

    _DELETE = "DELETE FROM Reserva WHERE IDReserva=?"

    _SELECT = "SELECT * FROM Reserva WHERE IDReserva=?"

    _CHECK_DISPONIBILIDAD = """
        SELECT COUNT(*) FROM Reserva 
        WHERE IDHabitacion = ? 
        AND (
            (FechaIngreso <= ? AND FechaSalida >= ?) OR 
            (FechaIngreso <= ? AND FechaSalida >= ?) OR
            (? <= FechaIngreso AND ? >= FechaSalida)
        )
    """

    @classmethod
    def insertar_reserva(cls, reserva):
        try:
            # Validación de ID duplicado solicitada
            if cls.existe_id_reserva(reserva.cod_reserva):
                return {'ejecuto': False, 'mensaje': 'El ID de Reserva ya existe.'}

            try:
                fecha_in = datetime.strptime(reserva.fecha_entrada, "%d/%m/%Y").strftime("%Y-%m-%d")
                fecha_out = datetime.strptime(reserva.fecha_salida, "%d/%m/%Y").strftime("%Y-%m-%d")
                with Conexion.obtenerCursor() as cursor:
                    datos = (reserva.cod_reserva, reserva.cliente, reserva.habitacion,
                             fecha_in, fecha_out, reserva.num_noches, reserva.estado)
                    cursor.execute(cls._INSERT, datos)
                    Conexion.obtenerConexion().commit()
                    respuesta = cursor.rowcount
                    if respuesta == 1:
                        return {'ejecuto': True, 'mensaje': 'Se guardo con exito.'}
            except bd.IntegrityError as e_bb:
                print(f"Error en la reserva: {e_bb}")
                if 'IDReserva' in e_bb.__str__():
                    return {'ejecuto': False, 'mensaje': 'Cedula ya existe.'}
                elif 'IDHuesped' in e_bb.__str__():
                    return {'ejecuto': False, 'mensaje': 'Cedula huespéd ya existe.'}
        except Exception as e:
            print(f"Error General: {e}")
            print(type(e))
            return {'ejecuto': False, 'mensaje': 'Error al guardar los datos, Comunicarse con Sistemas.'}

    @classmethod
    def actualizar_reserva(cls, reserva):
        try:
            fecha_in = datetime.strptime(reserva.fecha_entrada, "%d/%m/%Y").strftime("%Y-%m-%d")
            fecha_out = datetime.strptime(reserva.fecha_salida, "%d/%m/%Y").strftime("%Y-%m-%d")
            with Conexion.obtenerCursor() as cursor:
                datos = (reserva.cliente, reserva.habitacion, fecha_in,fecha_out, reserva.num_noches, reserva.estado,
                         reserva.cod_reserva)
                cursor.execute(cls._UPDATE, datos)
                # IMPORTANTE: Al usar pyodbc con SQL Server, recuerda hacer commit si no es automático
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Reserva actualizada con éxito.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'No se encontró la reserva para actualizar.'}
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al actualizar los datos.'}

    @classmethod
    def eliminar_reserva(cls, cod_reserva):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._DELETE, (cod_reserva,))
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Reserva eliminada correctamente.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'El código de reserva no existe.'}
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al intentar eliminar la reserva.'}

    @classmethod
    def seleccionar_reserva(cls, cod_reserva):
        try:
            with Conexion.obtenerCursor() as cursor:
                # Importante: Pasar como tupla (cod_reserva)
                cursor.execute(cls._SELECT, (cod_reserva,))
                registro = cursor.fetchone()

                if registro:
                    return Reserva(
                        cod_reserva=registro[0],
                        cliente=registro[1],
                        habitacion=registro[2],
                        fecha_entrada=registro[3],
                        fecha_salida=registro[4],
                        num_noches=registro[5],
                        estado=registro[6]
                    )
                return None
        except Exception as e:
            print(f"Error al seleccionar: {e}")
            return None

    @classmethod
    def validar_disponibilidad(cls, habitacion, f_entrada, f_salida, id_reserva_actual=None):
        try:
            with Conexion.obtenerCursor() as cursor:
                # Si estamos actualizando, debemos excluir la reserva actual de la búsqueda
                sql = cls._CHECK_DISPONIBILIDAD
                params = [habitacion, f_entrada, f_entrada, f_salida, f_salida, f_entrada, f_salida]

                if id_reserva_actual:
                    sql += " AND IDReserva <> ?"
                    params.append(id_reserva_actual)

                cursor.execute(sql, params)
                count = cursor.fetchone()[0]
                return count > 0  # Retorna True si ya está ocupada
        except Exception as e:
            print(f"Error al validar disponibilidad: {e}")
            return False

    @classmethod
    def existe_id_reserva(cls, id_reserva):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Reserva WHERE IDReserva = ?", (id_reserva,))
                resultado = cursor.fetchone()
                return resultado[0] > 0
        except Exception as e:
            print(f"Error al validar existencia de ID: {e}")
            return False