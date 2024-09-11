from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return None
        from app.models.usuario import Usuario
        return Usuario.query.get(user_id)

    from app.routes import usuarioRoutes, proveedorRoutes, mercanciaRoutes, ventaRoutes, menuRoutes, personalRoutes
    from app.routes.auth import auth_bp
    
    app.register_blueprint(usuarioRoutes.bp)
    app.register_blueprint(proveedorRoutes.bp)
    app.register_blueprint(mercanciaRoutes.bp)
    app.register_blueprint(menuRoutes.bp)
    app.register_blueprint(personalRoutes.bp)
    app.register_blueprint(ventaRoutes.bp)
    app.register_blueprint(auth_bp)

    return app
