from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from secrets import token_hex

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"

    from .auth import auth
    from .views import views


    app.register_blueprint(auth ,url_prefix='/')
    app.register_blueprint(views ,url_prefix='/')

    return app
