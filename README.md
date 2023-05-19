# PROYECTO_FINAL
UNA VEZ DESCARGADO EL PROYECTO CORRER PRIMERAMENTE EN LA TERMINAL EL COMANDO "python -m venv venv" dentro de la carpeta 
Proyecto_final, MEJOR SI SE USA VSCODE QUE YA ABRE LA TERMINAL EN LA CARPETA
DESPUES SI EL SISTEMA OPERATIVO ES WINDOWS ACTIVAR EL ENTORNO VIRTUAL CON "venv\Scripts\activate", USAR LA TERMINAL
UNA VEZ LA CARPETA venv (entorno virtual) ESTE ACTIVO CORRER EL COMANDO 
"pip install flask flask-cors flask-expects-json psycopg2 python-decouple python-dotenv" LIBRERIAS NECESARIAS PARA CORRER.
LUEGO CREAR EL ARCHIVO ".env" QUE DEBE CONTENER LAS CONFIGURACIONES NECESARIAS PARA LA CONEXION CON LA BASE DE DATOS:
SECRET_KEY=1234
PGSQL_HOST=localhost
PGSQL_USER=postgres
PGSQL_PASSWORD=1234
PGSQL_DATABASE=PERSONAS
PGSQL_PORT=5433
o puede usar los datos que mejor le sirvan
***************************************************************************************************************
RUTAS
***************************************************************************************************************
Para activar el servidor es necesario poner en la terminal de la carpeta:
python .\src\app.py
luego en el POSTMAN, las rutas son:
*ruta inicial que creará la base de datos y la tabla en caso de que no exista: localhost:5000
*Para obtener todos los usuarios la ruta es: GET localhost:5000/usuarios
*Para obtener a un sólo usuario por su id es: GET localhost:5000/usuarios/<id>
*Para insertar un nuevo usuario la ruta es: POST localhost:5000/usuarios Donde se debe ingresar en formato JSON
en el body los siguientes datos:
  {
      "cedula":6655661,
      "nombre":"BRYAN DANIEL",
      "apellido1":"ACOSTA",
      "apellido2":"QUISPE",
      "nacimiento":"15/12/2001"
  }
Tomar en cuenta que es posible enviar sólo un apellido ya que no todos contamos con 2 apellidos, pero es obligatorio 
tener al menos 1 apellido, tambien tener en cuenta que la fecha de nacimiento debe estar en formato fecha o no se podra registrar
*Para actualizar un usuario la ruta es: PUT localhost:5000/usuarios/<id> pero debe tener los mismos datos que la ruta insertar
por ejemplo: 
  {
      "cedula":6655661,
      "nombre":"BRYAN DANIEL",
      "apellido1":"ACOSTA",
      "apellido2":"QUISPE",
      "nacimiento":"15/12/2001"
  }
*Para eliminar un usuario la ruta es: DELETE localhost:5000/<id> es necesario conocer la id para eliminarlo de la base de datos
*Para ver la version, creador, email la ruta es: GET localhost:5000/estado
*Para ver la ruta que devuelve el promedio de edades: GET localhost:5000/usuarios/promedio-edad