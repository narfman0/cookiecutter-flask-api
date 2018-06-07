# -*- coding: utf-8 -*-
""" Test configs """
import json
from unittest import TestCase

from flask_webtest import TestApp

from {{cookiecutter.app_name}} import app


class AppTestCase(TestCase):

    def setUp(self):
        self.app = TestApp(app.create_app())

    def test_cats_get(self):
        rv = self.app.get('/api/v1/cats/')
        data = json.loads(rv.body)
        self.assertEquals(1, int(data[0]['id']))
