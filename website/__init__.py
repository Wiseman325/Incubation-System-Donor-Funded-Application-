from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from secrets import token_hex
from flask_login import LoginManager
from os import path

db = SQLAlchemy()  # Declare globally
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    
    # Initialize the database (setup app)
    db.init_app(app)

    from .auth import auth
    from .views import views
    from .account import account

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(account, url_prefix='/account')

    from .models import User

    create_database(app)

    # Set up LoginManager for user authentication
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
            print("Database created")
