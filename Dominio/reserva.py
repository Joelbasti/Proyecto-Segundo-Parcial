#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia

from Dominio.clientes import Clientes
from Dominio.habitacion import Habitacion

#esta es una superclase
class Reserva:
    '''
    Clase que permite crear objetos de tipo persona
    '''
    def __init__(self, cod_reserva: int, cliente: str, habitacion: int,
                 fecha_entrada: str, fecha_salida: str, num_noches: int, estado: str):
        self._cod_reserva = cod_reserva
        self._cliente = cliente
        self._habitacion = habitacion
        self._fecha_entrada = fecha_entrada
        self._fecha_salida = fecha_salida
        self._num_noches = num_noches
        self._estado = estado

    #metodos getter/setter & str
    @property
    def cod_reserva(self):
        return self._cod_reserva
    @cod_reserva.setter
    def cod_reserva(self, codigo: int):
        self._cod_reserva = codigo

    @property
    def cliente(self):
        return self._cliente
    @cliente.setter
    def cliente(self, cliente: Clientes):
        if not isinstance(cliente, Clientes):
            raise ValueError("Debe ser un objeto de tipo Clientes")
        self._cliente = cliente

    @property
    def habitacion(self):
        return self._habitacion
    @habitacion.setter
    def habitacion(self, habitacion: Habitacion):
        if not isinstance(habitacion, Habitacion):
            raise ValueError("Debe ser un objeto de tipo Habitacion")
        self._habitacion = habitacion

    @property
    def fecha_entrada(self):
        return self._fecha_entrada
    @fecha_entrada.setter
    def fecha_entrada(self, fecha: str):
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser texto")
        if not fecha.strip():
            raise ValueError("La fecha de entrada no puede estar vacía")
        self._fecha_entrada = fecha.strip()

    @property
    def fecha_salida(self):
        return self._fecha_salida
    @fecha_salida.setter
    def fecha_salida(self, fecha: str):
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser texto")
        if not fecha.strip():
            raise ValueError("La fecha de salida no puede estar vacía")
        self._fecha_salida = fecha.strip()

    @property
    def num_noches(self):
        return self._num_noches
    @num_noches.setter
    def num_noches(self, noches: int):
        if not isinstance(noches, int):
            raise ValueError("El número de noches debe ser un entero")
        if noches <= 0:
            raise ValueError("El número de noches debe ser mayor a 0")
        self._num_noches = noches

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado: str):
        if not isinstance(estado, str):
            raise ValueError("El estado debe ser texto")
        if not estado.strip():
            raise ValueError("El estado no puede estar vacío")
        estados_validos = ['pendiente', 'confirmada', 'cancelada', 'completada']
        if estado.lower() not in estados_validos:
            raise ValueError(f"Estado debe ser uno de: {', '.join(estados_validos)}")
        self._estado = estado.strip().lower()




