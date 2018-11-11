from flask import Flask, request
from flask import jsonify
from flask import render_template

from models import db
from models import Client, ProductArea, Feature
import util

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:testing@localhost/testdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


# Get all features
@app.route('/api/features', methods=['GET'])
def get_features():
    q = db.session.query(Feature)
    return jsonify([util.toDict(feature) for feature in q.all()])


# Add a feature
@app.route('/api/feature/new', methods=['POST'])
def new_feature():
    data = request.get_json()
    client = data.get('client')
    priority = data.get('priority')
    util.updatePriority(client, priority)
    db.session.add(Feature(data.get('title'), data.get('description'),
                           client, priority, data.get('target_date'), data.get('product_area')))
    db.session.commit()
    return jsonify(data)


# Edit a feature
@app.route('/api/feature/update', methods=['PATCH'])
def update_feature():
    data = request.get_json()
    client = data.get('client')
    priority = data.get('priority')
    feature = Feature.query.filter_by(id=data.get('id')).first()
    feature.title = data.get('title')
    feature.description = data.get('description')
    feature.target_date = data.get('target_date')
    feature.product_area = data.get('product_area')
    util.updatePriority(client, priority)
    feature.client = client
    feature.priority = priority

    db.session.commit()
    return jsonify(data)


# Delete a feature
@app.route('/api/feature/delete', methods=['DELETE'])
def delete_feature():
    data = request.get_json()
    Feature.query.filter_by(id=data.get('id')).delete()
    db.session.commit()
    return jsonify({'Status': 'success'}, 200)


if __name__ == "__main__":
    app.run(host='192.168.8.100')
