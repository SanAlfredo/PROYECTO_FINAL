from flask import Blueprint, jsonify

# importar la clase UserModel

from models.UserModel import UserModel

main = Blueprint('usuario_blue', __name__)


@main.route('/')
def get_usuarios():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
