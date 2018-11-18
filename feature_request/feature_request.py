import sys

from flask import Flask, request
from flask import jsonify, Blueprint
from flask import render_template
import datetime

from db_setup import dbsetup
from models import db
from models import Client, ProductArea, Feature
import util
import config

from app_factory import create_app

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return render_template('index.html')


# Get all features
@api.route('/api/features', methods=['GET'])
def get_features():
    query = Feature.query.order_by(Feature.priority)
    return jsonify([util.toDict(feature) for feature in query.all()])


# Add a feature
@api.route('/api/feature/new', methods=['POST'])
def new_feature():
    data = request.get_json()
    client = data.get('client')
    priority = data.get('priority')
    util.updatePriority(client, priority)
    db.session.add(Feature(data.get('title'), data.get('description'),
                           client, priority, datetime.datetime.strptime(
                               data.get('target_date'), '%Y-%m-%d'),
                           data.get('product_area')))
    db.session.commit()
    return jsonify({'Status': 'success'}, 200)


# Edit a feature
@api.route('/api/feature/update', methods=['PATCH'])
def update_feature():
    data = request.get_json()
    client = data.get('client')
    priority = data.get('priority')
    feature = Feature.query.filter_by(id=data.get('id')).first()
    feature.title = data.get('title')
    feature.description = data.get('description')
    feature.target_date = datetime.datetime.strptime(
        data.get('target_date'), '%Y-%m-%d')
    feature.product_area = data.get('product_area')
    util.updatePriority(client, priority)
    feature.client = client
    feature.priority = priority

    db.session.commit()
    return jsonify({'Status': 'success'}, 200)


# Delete a feature
@api.route('/api/feature/delete', methods=['DELETE'])
def delete_feature():
    data = request.get_json()
    Feature.query.filter_by(id=data.get('id')).delete()
    db.session.commit()
    return jsonify({'Status': 'success'}, 200)


if __name__ == "__main__":

    if len(sys.argv) > 1 :
        env = sys.argv[1]
    else:
        raise ValueError('Environment name required')

    if env == 'dev':
        app = create_app(config.DevelopmentConfig)
    elif env == 'prod':
        app = create_app(config.ProductionConfig)
    elif env == 'docker':
        app = create_app(config.DockerDeployConfig)
    else:
        raise ValueError('Invalid environment name')
    
    app.register_blueprint(api)
    dbsetup(db, app)
    app.run(host='0.0.0.0')
