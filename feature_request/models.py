from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Feature(db.Model):
    """
    Create a feature table
    """
    __tablename__ = 'feature'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client = db.Column(db.String(20), db.ForeignKey('client.name'))
    priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    product_area = db.Column(db.String(20), db.ForeignKey('product_area.name'))

    def __init__(self, title, desc, client, priority, tdate, area):
        self.title = title
        self.description = desc
        self.client = client
        self.priority = priority
        self.target_date = tdate
        self.product_area = area


class Client(db.Model):
    """
    Create a client table
    """

    __tablename__ = 'client'

    name = db.Column(db.String(20), primary_key=True, nullable=False)


class ProductArea(db.Model):
    """
    Create a product area table
    """

    __tablename__ = 'product_area'

    name = db.Column(db.String(20), primary_key=True, nullable=False)
