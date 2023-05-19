from flask import Blueprint, jsonify, request, make_response
from flask_expects_json import expects_json
import uuid
from jsonschema import ValidationError
from datetime import datetime


# importar la clase Usuario
from models.entities.User import User
# importar la clase UserModel
from models.UserModel import UserModel

main = Blueprint('usuario_blue', __name__)

# region ruta usuarios, get todo


@main.route('/')
def get_usuarios():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
# endregion

# region ruta usuario get 1 usuario por id


@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({"message":"no se pudo encontrar al usuario"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
# endregion


# esquema de validacion para datos de entrada en el json
schema = {
    "type": "object",
    "properties": {
        "cedula": {"type": "number"},
        "nombre": {"type": "string"},
        "apellido1": {"type": ["string", "null"]},
        "apellido2": {"type": ["string", "null"]},
        "nacimiento": {"type": "string"}
    },
    "required": ["cedula", "nombre", "apellido1", "apellido2", "nacimiento"]
}

# region Manejador de errores del esquema usado para validar datos de entrada


@main.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'error': original_error.message}), 400)
    # handle other "Bad Request"-errors
    return error
# endregion

# region ruta para insertar usuario


@main.route('/', methods=['POST'])
@expects_json(schema)
def add_user():
    if valDate(request.json['nacimiento']):
        if request.json['apellido1'] == "" and request.json['apellido2'] == "":
            return jsonify({"message": "Al menos un apellido se debe llenar"}), 404
        else:
            if request.json['apellido1'] == "" and request.json['apellido2'] != "":
                primer_apellido = "no hay apellido paterno"
                segundo_apellido = request.json["apellido2"].lower()
            if request.json['apellido2'] == "" and request.json['apellido1'] != "":
                primer_apellido = request.json["apellido1"].lower()
                segundo_apellido = "no hay apellido materno"
            if request.json['apellido1'] != "" and request.json['apellido2'] != "":
                primer_apellido = request.json["apellido1"].lower()
                segundo_apellido = request.json["apellido2"].lower()
            nombre = request.json['nombre'].lower()
            id = str(uuid.uuid4())
            cedula_identidad = request.json['cedula']
            fecha_nacimiento = request.json['nacimiento']

            try:
                user = User(id, cedula_identidad, nombre,
                            primer_apellido, segundo_apellido, fecha_nacimiento)
                resultado = UserModel.add_user(user)
                if resultado==1:
                    return jsonify(user.id)
                else:
                    return jsonify({'message': 'Error al insertar'}), 500
            except Exception as ex:
                return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({"message": "la fecha no tiene el formato correcto"}), 404
# endregion
# region ruta para actualizar al usuario


@main.route('/<id>', methods=['PUT'])
@expects_json(schema)
def update_user(id):
    if valDate(request.json['nacimiento']):
        if request.json['apellido1'] == "" and request.json['apellido2'] == "":
            return jsonify({"message": "Al menos un apellido se debe llenar"}), 404
        else:
            if request.json['apellido1'] == "" and request.json['apellido2'] != "":
                primer_apellido = "no hay apellido paterno"
                segundo_apellido = request.json["apellido2"].lower()
            if request.json['apellido2'] == "" and request.json['apellido1'] != "":
                primer_apellido = request.json["apellido1"].lower()
                segundo_apellido = "no hay apellido materno"
            if request.json['apellido1'] != "" and request.json['apellido2'] != "":
                primer_apellido = request.json["apellido1"].lower()
                segundo_apellido = request.json["apellido2"].lower()
            nombre = request.json['nombre'].lower()
            cedula_identidad = request.json['cedula']
            fecha_nacimiento = request.json['nacimiento']

            try:
                user = User(id, cedula_identidad, nombre,
                            primer_apellido, segundo_apellido, fecha_nacimiento)
                resultado = UserModel.update_user(user)
                if resultado==1:
                    return jsonify(user.id)
                else:
                    return jsonify({'message': 'Error al actualizar los campos'}), 500
            except Exception as ex:
                return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({"message": "la fecha no tiene el formato correcto"}), 404
# endregion
# region ruta usuario get 1 usuario por id


@main.route('/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User(id)
        resultado = UserModel.delete_user(user)
        if resultado==1:
            return jsonify({"message": "Eliminado con éxito"})
        else:
            return jsonify({"message": "El archivo ya fue eliminado, no existe en la base de datos"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
# endregion
# region Validar el formato de la fecha

#region Promedio de edad
@main.route('/promedio-edad')
def promedio():
    try:
        users = UserModel.promedio_users()
        return jsonify({"promedioEdad":users})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
#endregion

def valDate(fecha):
    try:
        date = datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False
# endregion
