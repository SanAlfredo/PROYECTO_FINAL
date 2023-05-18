from flask import Blueprint, jsonify, request
import uuid

#importar la clase Usuario
from models.entities.User import User
# importar la clase UserModel
from models.UserModel import UserModel

main = Blueprint('usuario_blue', __name__)

#ruta usuarios, get todo
@main.route('/')
def get_usuarios():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#ruta usuario get 1
@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#ruta para insertar usuario
@main.route('/', methods=['POST'])
def add_user():
    try:
        id=str(uuid.uuid4())
        cedula_identidad=request.json['cedula_identidad']
        nombre=request.json['nombre']
        primer_apellido=request.json['primer_apellido']
        segundo_apellido=request.json['segundo_apellido']
        fecha_nacimiento=request.json['fecha_nacimiento']
        user=User(id,cedula_identidad,nombre,primer_apellido,segundo_apellido,fecha_nacimiento)
        resultado= UserModel.add_user(user)
        if resultado ==1:
            return jsonify(user.id)
        else:
            return jsonify({'message':'Error al insertar'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
