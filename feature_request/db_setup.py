from flask import Flask
from models import db, Client, ProductArea
from feature_request import app

#app = Flask(__name__)


def dbsetup():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:testing@localhost/testdb'
    # db.init_app(app)
    db.app = app
    db.create_all()
    insert_initial_values()


def insert_initial_values():
    # Add default clients
    db.session.add(Client(name='Client A'))
    db.session.add(Client(name='Client B'))
    db.session.add(Client(name='Client C'))

    # Add default ProductArea
    db.session.add(ProductArea(name='Policies'))
    db.session.add(ProductArea(name='Billing'))
    db.session.add(ProductArea(name='Claims'))
    db.session.add(ProductArea(name='Reports'))

    # Commit to database
    db.session.commit()


dbsetup()
