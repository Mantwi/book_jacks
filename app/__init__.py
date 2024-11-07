from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # app/__init__.py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Keepmesafe90@pre-reg.cluc8o6wyyjf.us-west-1.rds.amazonaws.com:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) 

    with app.app_context():
        from . import  models

        db.create_all()

    return app
