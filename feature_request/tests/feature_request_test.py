import os
import unittest
import tempfile
import json

from flask import Flask

import config
from app_factory import create_app
from db_setup import dbsetup
from models import db
from feature_request import api

app = create_app(config.TestingConfig)

htype = 'application/json'
headers = {
    'Content-Type': htype,
    'Accept': htype
}
test_feature = {
    'id': '1',
    'title': 'test feature',
    'description': 'test description',
    'client': 'Client A',
    'priority': 1,
    'target_date': '2018-12-12',
    'product_area': 'Billing'}


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True
        app.register_blueprint(api)
        db.init_app(app)
        dbsetup(db, app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_features_no_feature(self):
        response = self.app.get('/api/features')
        self.assertEqual(response.get_data(as_text=True), '[]\n')

    def test_add_feature(self):
        response = self.app.post('/api/feature/new',
                                 data=json.dumps(test_feature),
                                 headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_features_add_feature(self):
        self.test_add_feature()
        response = self.app.get('/api/features')
        json_resp = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_resp), 1)
        self.assertEqual(json_resp[0]['title'], 'test feature')
        self.assertEqual(json_resp[0]['description'], 'test description')
        self.assertEqual(json_resp[0]['client'], 'Client A')
        self.assertEqual(json_resp[0]['priority'], 1)
        self.assertEqual(json_resp[0]['target_date'], '2018-12-12')
        self.assertEqual(json_resp[0]['product_area'], 'Billing')

    def test_update_feature(self):
        self.test_add_feature()
        test_feature['client'] = 'Client B'
        response = self.app.patch('/api/feature/update',
                                  data=json.dumps(test_feature),
                                  headers=headers)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/api/features')
        json_resp = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_resp[0]['title'], 'test feature')
        self.assertNotEqual(json_resp[0]['client'], 'Client A')
        self.assertEqual(json_resp[0]['client'], 'Client B')

    def test_priority_auto_update(self):
        self.test_add_feature()
        response = self.app.patch('/api/feature/update',
                                  data=json.dumps(test_feature),
                                  headers=headers)
        self.assertEqual(response.status_code, 200)
        test_feature2 = dict(test_feature)
        test_feature2['title'] = 'test feature2'
        self.assertEqual(test_feature['title'], 'test feature')
        self.assertEqual(test_feature2['priority'], 1)
        self.assertEqual(test_feature['priority'], 1)
        response = self.app.post('/api/feature/new',
                                 data=json.dumps(test_feature2),
                                 headers=headers)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/api/features')
        json_resp = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_resp), 2)
        self.assertEqual(json_resp[1]['title'], 'test feature')
        self.assertEqual(json_resp[1]['priority'], 2)
        self.assertEqual(json_resp[0]['title'], 'test feature2')
        self.assertEqual(json_resp[0]['priority'], 1)

    def test_delete_feature(self):
        self.test_add_feature()
        response = self.app.get('/api/features')
        json_resp = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_resp), 1)
        response = self.app.delete('/api/feature/delete',
                                   data=json.dumps(test_feature),
                                   headers=headers)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/api/features')
        json_resp = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_resp), 0)


if __name__ == '__main__':
    unittest.main()
