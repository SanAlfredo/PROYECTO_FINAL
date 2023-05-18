from database.db import get_connection1, get_connection


class CrearDB():

    @classmethod
    def crear_base_de_datos(self):
        x=0
        try:
            conn1 = get_connection1()
            conn1.close()
            x=1
        except:
            x=0
        if x==1:
            return False
        else:
            try:
                conn = get_connection()
                conn.autocommit = True
                with conn.cursor() as cursor:
                    cursor.execute('''CREATE DATABASE "PERSONAS"''')
                    cursor.close()
                conn.close()
                conn1 = get_connection1()
                conn1.autocommit = True
                with conn1.cursor() as cursor1:
                    cursor1.execute('''
                        CREATE TABLE IF NOT EXISTS USUARIOS(
                            ID CHARACTER(36),
                            CEDULA_IDENTIDAD INT,
                            NOMBRE VARCHAR(30),
                            PRIMER_APELLIDO VARCHAR(30),
                            SEGUNDO_APELLIDO VARCHAR(30),
                            FECHA_NACIMIENTO DATE,
                            PRIMARY KEY (ID));
                        ''')
                conn1.close()
                return True
            except Exception as ex:
                raise ex

        
