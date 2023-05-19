from database.db import get_connection1
from .entities.User import User


class UserModel():
    # NOTA: los códigos comentados fueron usados en otra tabla y base de datos con la finalidad
    # de probar los metodos GET, pero para los metodos POST,PUT y DELETE ya se prueba en la base
    # de datos hecha para esta API

    # class method para instanciarlo de donde sea
    # region obtenemos todos los usuarios
    @classmethod
    def get_users(self):
        try:
            users = []
            conn = get_connection1()
            with conn.cursor() as cursor:
                # cursor.execute("SELECT * FROM persona")
                cursor.execute("SELECT * FROM usuarios")
                resultado = cursor.fetchall()
                for u in resultado:
                    user = User(u[0], u[1], u[2], u[3], u[4], u[5])
                    users.append(user.to_JSON())
            conn.close()
            return users
        except Exception as ex:
            raise ex
    # endregion
    # region obtenemos solo 1 usuario

    @classmethod
    def get_user(self, id_usuario):
        try:
            conn = get_connection1()
            with conn.cursor() as cursor:
                # cursor.execute("SELECT * FROM persona where id_persona = %s",(id_usuario,))
                cursor.execute(
                    "SELECT * FROM usuarios where id = %s", (id_usuario,))
                resultado = cursor.fetchone()
                user = None
                if resultado != None:
                    user = User(resultado[0], resultado[1], resultado[2],
                                resultado[3], resultado[4], resultado[5])
                    user = user.to_JSON()
            conn.close()
            return user
        except Exception as ex:
            raise ex
    # endregion
    # region insertar un usuario

    @classmethod
    def add_user(self, user):
        try:
            conn = get_connection1()
            with conn.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios (id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
                                VALUES (%s,%s,%s,%s,%s,%s)""", (user.id, user.cedula_identidad, user.nombre, user.primer_apellido,
                                                                user.segundo_apellido, user.fecha_nacimiento),)
                #filas = cursor.rowcount()
                conn.commit()
            conn.close()
            return True
        except:
            return False    
    # endregion

    # region elimina un usuario

    @classmethod
    def delete_user(self, user):
        try:
            conn = get_connection1()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id = %s", (user.id,))
                conn.commit()
            conn.close()
            return True
        except Exception:
            return False    
    # endregion
