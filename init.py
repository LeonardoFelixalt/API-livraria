from flask import Flask
from .routes.livros import bp as livros_bp
from .routes.autores import bp as autores_bp
from .routes.clientes import bp as clientes_bp

def create_app():
    app = Flask(__name__)

    # Registrar as rotas
    app.register_blueprint(livros_bp)
    app.register_blueprint(autores_bp)
    app.register_blueprint(clientes_bp)

    return app
