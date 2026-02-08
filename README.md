SISTEMA DE ADMINISTRACIÓN DE RESERVA HOTELERA SARH
-DESCRIPCIÓN GENERAL DEL PROYECTO
Este programa provee una interfaz gráfica de fácil uso para controlar un sistema de reservas hoteleras conectada a una base de datos para asegurar la persistencia de la información
permitiendo realizar consultas, editar, eliminar y agendar reservas (CRUD)

-TECNOLOGÍA APLICADAS
Esta diseñado en lenguaje Python empleando apps externas como Qtdesigner mediante librerias como PySide6, por otro lado, emplea SQL MANAGEMENT STUDIO 21 para almacenar los datos 
y un ODBC para comunicar el programa con la base para realizar los comandos DML

-ARQUITECTURA DEL PROYECTO SARH
El proyecto esta estructurado en 4 Directorios:

DATOS: 
Este directorio almacena 2 archivos Conexion y Reserva_DAO:
CONEXION:
Importa las librerias sys y pyodbc para que la clase conexion se encargue de establecer la conexión a la BBDD y cursor mediante los metodos de clase obtenerConexion y obtenerCursor

RESERVA_DAO:
Importa las librerias pyodbc y date, además de directorios Dominio y Datos que usa la clase ReservaDAO encargada de almacenar las intrucciones DML y los métodos de clases 
necesarios para poder ejecutarlos, con sus respectivas def de validaciones para evitar conflictos con la DB en la ejecución de las instrucciones.
---------------------------------------------------------------
DOMINIO:
Este directorio almacena los archivos que definen los atributos de la clase principal y las clases de composión que usa el programa, además de sus respectivos encapsulamientos.
CLIENTES: Clase de composición que crea objetos de tipo clientes, estableciendo los atributos que recibe la clase y sus métodos @PROPERTY & SETTER.

HABITACIÓN: Clase de composición que crea objetos de tipo habitación, estableciendo los atributos que recibe la clase y sus métodos @PROPERTY & SETTER.

RESERVA:Clase Principal que se Compone de las clases clientes y habitacion para crear objetos de tipo reserva, estableciendo los atributos que recibe la clase y sus métodos @PROPERTY & SETTER.
----------------------------------------------------------------
SERVICIO:
Este directorio almacena el archivo reserva que define la clase ReservaServicio
RESERVASERVICIO: clase que genera lo lógica de los objetos de tipo reserva, define funciones que implementarán las instrucciones DML. Además establece la conexión de los botones
con sus respectivas funciones.
----------------------------------------------------------------
UI:
Directorio que almacena 2 archivos interfaz.ui y vtnPrincipal
INTERFAZ.UI: Archivo generado por Qtdesigner que define las propiedades de la interfaz gráfica: Botones, campos TxT y lbl.

vtnPrincipal: Archivo generado de la traducción del lenguaje de Qtdesigner (xml) a Python para que pueda ser entendido por el programa y establecer las respectivas conexiones.
----------------------------------------------------------------
MAIN: archivo que da arranque al programa.

-CAPTURAS DE PANTALLA DE LA EJECUCIÓN
BUSCAR
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ca6e7aea-9acc-4a7c-9957-c639171c3d5b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/10a89cb4-af3d-4ff6-b512-b2d6495b9d59" />

ACTUALIZAR
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/94b6b53d-a4e6-4b94-9c20-95cb47a067fd" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/23d21177-f052-4460-b078-8607cb9955c8" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/223adfd8-3875-4000-bf74-16edf7e8e2da" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/397e89cf-1842-4273-ae4b-a75a98ef7610" />

ELIMINAR 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b005f5c2-9d6b-4b97-84d8-488886598288" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fb241697-b10e-472a-9f14-123471422651" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/799a519e-6fed-445f-9230-31d5baadc0e7" />

INSERTAR
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7aaf9707-6ce4-4fa4-ae0e-f38400b93039" />


VALIDACIONES
campo de cliente vacío
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/334aac99-dd29-45c2-89b3-1de6fab83d0d" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1a375bf2-1ca1-4a58-b4d2-b31dd72c75e0" />

campo de reserva vacío
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7e1aa8ca-cf0a-4502-b0f3-19efd77e23bf" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/674c1b0f-f4c4-441a-9125-b6c2ae701204" />


LINK DEL VIDEO EXPLICATIVO
https://www.loom.com/share/ce9bd2dbdc0b4e47b59acce9c0d94b6d


