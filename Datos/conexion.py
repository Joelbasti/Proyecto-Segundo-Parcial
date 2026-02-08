#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia


import sys
import pyodbc as bd
class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    _SERVIDOR = 'KURODSKTP'
    _BBDD = 'SARH'
    _USUARIO = 'admin_sarh'
    _PASSWORD = '231022'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        #Obtiene la conexion a la BBDD con los parametros de conexion pasados como constantes

        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                    cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                                           + ';TrustServerCertificate=yes')
                return cls._conexion
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._conexion
    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor que
        :return:
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                return cls._cursor
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())
