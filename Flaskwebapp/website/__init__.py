from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db" # name of the database is given here

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ghosty'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # data is being stored in the loaction given in the f string in the website folder
    db.init_app(app) # initialize the database by providing the flask app 



    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,Note #function -->(models.py file runs before we create the database)
    with app.app_context():
     db.create_all()

    login_manager=LoginManager()
    login_manager.login_view='auth.login' # where the flask will redirect us if the user is not logged in or there is a login required
    login_manager.init_app(app) # telling the login manager which app we are using

    @login_manager.user_loader
    def load_user(id):
       return User.query.get(int(id))

    return app


