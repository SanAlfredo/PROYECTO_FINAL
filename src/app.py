from flask import Flask,jsonify
from config import config
from database.CrearDB import CrearDB

# importamos rutas
from routes import UserRoute

app = Flask(__name__)

#ruta inicial index
@app.route('/')
def index():
    if CrearDB.crear_base_de_datos():
        return "<h1>BASE DE DATOS CREADA Y LISTA PARA USARSE</h1>"
    else:
        return "<h1>LA BASE DE DATOS YA EXISTE</h1>"
    
#ruta estado    
@app.route('/estado')
def estado():
    data={
        'nameSystem':'api-users',
        'version': '0.0.1',
        'developer':'Alfredo Valverde Aranibar',
        'email':'alfredo.2009.8@gmail.com'
    }
    return jsonify(data)
def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    # Blueprints asignar rutas
    app.register_blueprint(UserRoute.main, url_prefix='/usuarios')
    # manejador de errores
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
