from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from secrets import token_hex
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "app.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    # initialise the database (setup app)
    db.init_app(app)

    from .auth import auth
    from .views import views
    from .account import account


    app.register_blueprint(auth ,url_prefix='/')
    app.register_blueprint(views ,url_prefix='/')
    app.register_blueprint(account ,url_prefix='/account')

    return app
