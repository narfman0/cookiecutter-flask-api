# -*- coding: utf-8 -*-
""" Test configs """
import json
from unittest import TestCase

from {{cookiecutter.app_name}} import app


class AppTestCase(TestCase):
    def setUp(self):
        self.app = app.create_app().test_client()
        self.app.testing = True

    def test_root(self):
        rv = self.app.get("/api/v1/")
        self.assertEqual(200, rv.status_code)

    def test_swagger(self):
        rv = self.app.get("/api/v1/swagger.json")
        self.assertEqual(200, rv.status_code)
        data = json.loads(rv.data)
        self.assertTrue(len(data["paths"]) > 0)

    def test_cats_get(self):
        rv = self.app.get("/api/v1/cats/")
        data = json.loads(rv.data)
        self.assertEquals(1, int(data[0]["id"]))
