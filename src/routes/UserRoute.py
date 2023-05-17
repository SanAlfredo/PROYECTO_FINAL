from flask import Blueprint, jsonify

main=Blueprint('usuario_blue',__name__)

@main.route('/')
def get_usuarios():
    return jsonify({'message':'Usuarios encontrados'})