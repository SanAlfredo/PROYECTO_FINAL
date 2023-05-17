from database.db import get_connection1
from .entities.User import User

class UserModel():

    #class method para instanciarlo de donde sea
    @classmethod
    def get_users(self):
        try:
            conn = get_connection1()
            users=[]
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM USUARIOS")
                resultado=cursor.fetchall()
                
                for u in resultado:
                    user = User(u[0],u[1],u[2],u[3],u[4],u[5])
                    users.append(user)
            conn.close()
            return users
        except Exception as ex:
            raise ex