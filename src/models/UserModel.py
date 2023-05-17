from database.db import get_connection1
from .entities.User import User


class UserModel():

    # class method para instanciarlo de donde sea
    #obtenemos todos los usuarios
    @classmethod
    def get_users(self):
        try:
            conn = get_connection1()
            users = []
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM persona")
                resultado = cursor.fetchall()
                for u in resultado:
                    user = User(u[0], u[1], u[2], u[3], u[4], u[5])
                    users.append(user.to_JSON())
            conn.close()
            return users
        except Exception as ex:
            raise ex
    #obtenemos solo 1 usuario
    @classmethod
    def get_user(self,id_usuario):
        try:
            conn = get_connection1()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM persona where id_persona = %s",(id_usuario,))
                resultado = cursor.fetchone()
                user = None
                if resultado != None:
                    user = User(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                    user=user.to_JSON()
            conn.close()
            return user
        except Exception as ex:
            raise ex