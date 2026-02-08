#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(444, 810)
        self.lblCodigoReserva = QLabel(vtnPrincipal)
        self.lblCodigoReserva.setObjectName(u"lblCodigoReserva")
        self.lblCodigoReserva.setGeometry(QRect(70, 110, 131, 31))
        self.TxTCodigoReserva = QLineEdit(vtnPrincipal)
        self.TxTCodigoReserva.setObjectName(u"TxTCodigoReserva")
        self.TxTCodigoReserva.setGeometry(QRect(210, 110, 161, 31))
        self.TxTCodigoReserva.setMaxLength(5)
        self.btnGuardar = QPushButton(vtnPrincipal)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(60, 750, 131, 41))
        self.btnLimpiar = QPushButton(vtnPrincipal)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(250, 750, 131, 41))
        self.lblCedulaHuesped = QLabel(vtnPrincipal)
        self.lblCedulaHuesped.setObjectName(u"lblCedulaHuesped")
        self.lblCedulaHuesped.setGeometry(QRect(70, 160, 131, 31))
        self.TxTCedulaHuesped = QLineEdit(vtnPrincipal)
        self.TxTCedulaHuesped.setObjectName(u"TxTCedulaHuesped")
        self.TxTCedulaHuesped.setGeometry(QRect(210, 160, 161, 31))
        self.TxTCedulaHuesped.setMaxLength(10)
        self.lblHabitacion = QLabel(vtnPrincipal)
        self.lblHabitacion.setObjectName(u"lblHabitacion")
        self.lblHabitacion.setGeometry(QRect(70, 210, 131, 31))
        self.TxTHabitacion = QLineEdit(vtnPrincipal)
        self.TxTHabitacion.setObjectName(u"TxTHabitacion")
        self.TxTHabitacion.setGeometry(QRect(210, 210, 161, 31))
        self.lblFechaIngreso = QLabel(vtnPrincipal)
        self.lblFechaIngreso.setObjectName(u"lblFechaIngreso")
        self.lblFechaIngreso.setGeometry(QRect(70, 260, 131, 31))
        self.lblFechaEngreso = QLabel(vtnPrincipal)
        self.lblFechaEngreso.setObjectName(u"lblFechaEngreso")
        self.lblFechaEngreso.setGeometry(QRect(70, 310, 131, 31))
        self.dateFechaEntrada = QDateEdit(vtnPrincipal)
        self.dateFechaEntrada.setObjectName(u"dateFechaEntrada")
        self.dateFechaEntrada.setGeometry(QRect(210, 260, 121, 31))
        self.dateFechaEntrada.setCalendarPopup(True)
        self.dateFechaSalida = QDateEdit(vtnPrincipal)
        self.dateFechaSalida.setObjectName(u"dateFechaSalida")
        self.dateFechaSalida.setGeometry(QRect(210, 310, 121, 31))
        self.dateFechaSalida.setCalendarPopup(True)
        self.lblNumeroNoches = QLabel(vtnPrincipal)
        self.lblNumeroNoches.setObjectName(u"lblNumeroNoches")
        self.lblNumeroNoches.setGeometry(QRect(70, 360, 131, 31))
        self.spinBox = QSpinBox(vtnPrincipal)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(210, 360, 121, 31))
        self.spinBox.setMaximum(365)
        self.lblEstadoReserva = QLabel(vtnPrincipal)
        self.lblEstadoReserva.setObjectName(u"lblEstadoReserva")
        self.lblEstadoReserva.setGeometry(QRect(70, 410, 141, 31))
        self.comboBox = QComboBox(vtnPrincipal)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 410, 121, 31))
        self.groupBox = QGroupBox(vtnPrincipal)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 500, 301, 161))
        self.btnCrearReserva = QPushButton(self.groupBox)
        self.btnCrearReserva.setObjectName(u"btnCrearReserva")
        self.btnCrearReserva.setGeometry(QRect(10, 30, 121, 23))
        self.btnBuscarReserva = QPushButton(self.groupBox)
        self.btnBuscarReserva.setObjectName(u"btnBuscarReserva")
        self.btnBuscarReserva.setGeometry(QRect(10, 60, 121, 23))
        self.btnActualizar = QPushButton(self.groupBox)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(10, 90, 121, 23))
        self.btnEliminarReserva = QPushButton(self.groupBox)
        self.btnEliminarReserva.setObjectName(u"btnEliminarReserva")
        self.btnEliminarReserva.setGeometry(QRect(10, 120, 121, 23))
        self.btnOk = QPushButton(self.groupBox)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setGeometry(QRect(180, 70, 75, 31))

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Reserva  de Habitaciones", None))
        self.lblCodigoReserva.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00d3DIGO DE RESERVA", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.lblCedulaHuesped.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00c9DULA HU\u00c9SPED", None))
        self.lblHabitacion.setText(QCoreApplication.translate("vtnPrincipal", u"HABITACI\u00d3N", None))
        self.lblFechaIngreso.setText(QCoreApplication.translate("vtnPrincipal", u"FECHA ENTRADA:", None))
        self.lblFechaEngreso.setText(QCoreApplication.translate("vtnPrincipal", u"FECHA SALIDA:", None))
        self.lblNumeroNoches.setText(QCoreApplication.translate("vtnPrincipal", u"N.\u00ba DE  NOCHES", None))
        self.lblEstadoReserva.setText(QCoreApplication.translate("vtnPrincipal", u"ESTADO CONFIRMACI\u00d3N", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"SELECCIONAR", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"PENDIENTE", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"CONFIRMADA", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"CANCELADA", None))

        self.groupBox.setTitle(QCoreApplication.translate("vtnPrincipal", u"HERRAMIENTAS CRUD", None))
        self.btnCrearReserva.setText(QCoreApplication.translate("vtnPrincipal", u"NUEVA RESERVA", None))
        self.btnBuscarReserva.setText(QCoreApplication.translate("vtnPrincipal", u"BUSCAR", None))
        self.btnActualizar.setText(QCoreApplication.translate("vtnPrincipal", u"ACTUALIZAR", None))
        self.btnEliminarReserva.setText(QCoreApplication.translate("vtnPrincipal", u"ELIMINAR RESERVA", None))
        self.btnOk.setText(QCoreApplication.translate("vtnPrincipal", u"OK", None))
    # retranslateUi

