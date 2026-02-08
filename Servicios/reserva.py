#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QMainWindow, QMessageBox
from UI.vtnPricipal import  Ui_vtnPrincipal
from Datos.reserva_DAO import ReservaDAO
from Dominio.reserva import Reserva


class ReservaServicio(QMainWindow, Ui_vtnPrincipal):
    '''
    Clase que genera la logica de los objetos de tipo reserva
    '''
    def __init__(self):
        super(ReservaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.dateFechaEntrada.dateChanged.connect(self.calcular_noches)
        self.ui.dateFechaSalida.dateChanged.connect(self.calcular_noches)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnCrearReserva.clicked.connect(self.crear)
        self.ui.btnBuscarReserva.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminarReserva.clicked.connect(self.eliminar)
        self.ui.btnOk.clicked.connect(self.ok)
        self.calcular_noches()
        self.limpiar()

    def calcular_noches(self):
        f_entrada = self.ui.dateFechaEntrada.date()
        f_salida = self.ui.dateFechaSalida.date()
        total = f_entrada.daysTo(f_salida)
        self.ui.spinBox.setValue(max(0, total))

    def validaciones(self):
        # Captura de datos del formulario
        cod_reserva = self.ui.TxTCodigoReserva.text().strip()
        cliente = self.ui.TxTCedulaHuesped.text().strip()
        habitacion = self.ui.TxTHabitacion.text().strip()
        fecha_entrada = self.ui.dateFechaEntrada.text().strip()
        fecha_salida = self.ui.dateFechaSalida.text().strip()
        noches = self.ui.spinBox.value()
        estado_reserva = self.ui.comboBox.currentText()

        # Lógica de validación
        if cod_reserva == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el Código de Reserva")
        elif len(cliente) < 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la cédula del huésped")
        elif habitacion == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el número de habitación")
        elif fecha_entrada == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la fecha de entrada")
        elif fecha_salida == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la fecha de salida")
        elif noches == 0:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el numero de noches")
        elif estado_reserva == "SELECCIONAR":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el estado de reserva")
        else:
            # Si pasa todas las validaciones, retorna el objeto Reserva
            return Reserva(cod_reserva=cod_reserva, cliente=cliente, habitacion=habitacion,
                           fecha_entrada=fecha_entrada, fecha_salida=fecha_salida,
                           num_noches=noches, estado=estado_reserva)
        return None

    def guardar(self):
        reserva = self.validaciones()
        if reserva:
            # VALIDACIÓN DE DUPLICADOS
            f_in = QDate.fromString(reserva.fecha_entrada, "d/M/yyyy").toString("yyyy-MM-dd")
            f_out = QDate.fromString(reserva.fecha_salida, "d/M/yyyy").toString("yyyy-MM-dd")

            ocupado = ReservaDAO.validar_disponibilidad(reserva.habitacion, f_in, f_out)

            if ocupado:
                QMessageBox.warning(self, "Habitación Ocupada",
                                    f"La habitación {reserva.habitacion} ya tiene una reserva en esas fechas.")
                return

            respuesta_dict = ReservaDAO.insertar_reserva(reserva)
            if respuesta_dict.get('ejecuto'):
                print(reserva)
                self.statusBar().showMessage("Se guardó la información", 5000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', respuesta_dict['mensaje'])

    def limpiar(self):
        self.ui.TxTCodigoReserva.clear()
        self.ui.TxTCedulaHuesped.clear()
        self.ui.TxTHabitacion.clear()
        hoy = QDate.currentDate()
        self.ui.dateFechaEntrada.setDate(hoy)
        self.ui.dateFechaSalida.setDate(hoy)
        self.ui.spinBox.setValue(0)
        self.ui.comboBox.setCurrentIndex(0)


    def crear(self):
        self.limpiar()
        self.statusBar().showMessage("Campos listos para nueva reserva.", 3000)


        pass

    def buscar(self):
            cod = self.ui.TxTCodigoReserva.text().strip()
            if not cod:
                QMessageBox.warning(self, "Advertencia", "Ingrese un código para buscar.")
                return

            reserva = ReservaDAO.seleccionar_reserva(cod)
            if reserva:
                self.ui.TxTCedulaHuesped.setText(str(reserva.cliente))
                self.ui.TxTHabitacion.setText(str(reserva.habitacion))
                f_entrada_str = str(reserva.fecha_entrada)[:10]
                f_salida_str = str(reserva.fecha_salida)[:10]
                self.ui.dateFechaEntrada.setDate(QDate.fromString(f_entrada_str, "yyyy-MM-dd"))
                self.ui.dateFechaSalida.setDate(QDate.fromString(f_salida_str, "yyyy-MM-dd"))
                self.ui.comboBox.setCurrentText(reserva.estado.upper())
                self.statusBar().showMessage("Reserva cargada con éxito.", 3000)
            else:
                QMessageBox.information(self, "Búsqueda", "No se encontró la reserva.")

    def actualizar(self):
        reserva_nueva = self.validaciones()

        if reserva_nueva:
            reserva_existente = ReservaDAO.seleccionar_reserva(reserva_nueva.cod_reserva)

            if reserva_existente:
                #Validar disponibilidad de habitación (traslape de fechas)
                f_in = QDate.fromString(reserva_nueva.fecha_entrada, "d/M/yyyy").toString("yyyy-MM-dd")
                f_out = QDate.fromString(reserva_nueva.fecha_salida, "d/M/yyyy").toString("yyyy-MM-dd")

                ocupado = ReservaDAO.validar_disponibilidad(
                    reserva_nueva.habitacion, f_in, f_out, reserva_nueva.cod_reserva
                )

                if ocupado:
                    QMessageBox.warning(self, "Conflicto de Fechas",
                                        "No se puede actualizar: La habitación ya está reservada para este periodo.")
                    return

                #Confirmación del usuario mediante botones
                mensaje = f"¿Desea actualizar la información de la reserva {reserva_nueva.cod_reserva}?"
                confirmar = QMessageBox.question(self, "Confirmar", mensaje,
                                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                if confirmar == QMessageBox.StandardButton.Yes:
                    #Ejecutar la actualización en el DAO
                    respuesta = ReservaDAO.actualizar_reserva(reserva_nueva)
                    if respuesta.get('ejecuto'):
                        QMessageBox.information(self, "Éxito", "Datos actualizados correctamente.")
                        self.buscar()  # Refresca la información en pantalla
                    else:
                        QMessageBox.critical(self, "Error", respuesta.get('mensaje'))
            else:
                # Este else corresponde a 'if reserva_existente'
                QMessageBox.warning(self, "Advertencia", "El código de reserva no existe en la base de datos.")


    def eliminar(self):
        cod = self.ui.TxTCodigoReserva.text().strip()
        if not cod:
            QMessageBox.warning(self, "Advertencia", "Seleccione una reserva para eliminar.")
            return

        # Cambia la forma en que llamas a los botones
        confirmar = QMessageBox.question(self, "Confirmar", f"¿Eliminar reserva {cod}?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirmar == QMessageBox.StandardButton.Yes:
            respuesta = ReservaDAO.eliminar_reserva(cod)
            if respuesta.get('ejecuto'):
                self.statusBar().showMessage(respuesta.get('mensaje'), 5000)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", respuesta.get('mensaje'))

    def ok(self):
        self.close()
