# PROYECTO_FINAL
UNA VEZ DESCARGADO EL PROYECTO CORRER PRIMERAMENTE EN LA TERMINAL EL COMANDO "python -m venv venv" dentro de la carpeta Proyecto_final, MEJOR SI SE USA VSCODE QUE YA ABRE LA TERMINAL EN LA CARPETA
DESPUES SI EL SISTEMA OPERATIVO ES WINDOWS ACTIVAR EL ENTORNO VIRTUAL CON "venv\Scripts\activate", USAR LA TERMINAL
UNA VEZ LA CARPETA venv (entorno virtual) ESTE ACTIVO CORRER EL COMANDO "pip install flask flask-cors psycopg2 python-decouple python-dotenv" LIBRERIAS NECESARIAS PARA CORRER.
LUEGO CREAR EL ARCHIVO ".env" QUE DEBE CONTENER LAS CONFIGURACIONES NECESARIAS PARA LA CONEXION CON LA BASE DE DATOS:
  SECRET_KEY=1234
  PGSQL_HOST=localhost
  PGSQL_USER=postgres
  PGSQL_PASSWORD=1234