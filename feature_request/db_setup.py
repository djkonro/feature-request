from flask import Flask
from models import Client, ProductArea

def dbsetup(db, app):
    db.app = app
    db.create_all()
    insert_initial_values(db)

def insert_initial_values(db):
    if len(Client.query.all()) == 0:
        # Add default clients
        db.session.add(Client(name='Client A'))
        db.session.add(Client(name='Client B'))
        db.session.add(Client(name='Client C'))
        db.session.commit()
    
    if len(ProductArea.query.all()) == 0:
        # Add default ProductArea
        db.session.add(ProductArea(name='Policies'))
        db.session.add(ProductArea(name='Billing'))
        db.session.add(ProductArea(name='Claims'))
        db.session.add(ProductArea(name='Reports'))
        db.session.commit()
