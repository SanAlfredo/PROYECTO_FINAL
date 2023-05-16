from flask import Flask, render_template
from config import config

#importamos rutas
from routes import Usuario

app = Flask(__name__)


def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    #Blueprints asignar rutas
    app.register_blueprint(Usuario.main,url_prefix='/usuarios')
    # manejador de errores
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
