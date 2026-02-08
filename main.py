#Grupo 6
#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia

import sys
from PySide6.QtWidgets import QApplication
from Servicios.reserva import ReservaServicio


app = QApplication()
vtn_principal = ReservaServicio()
vtn_principal.show()
sys.exit(app.exec())
