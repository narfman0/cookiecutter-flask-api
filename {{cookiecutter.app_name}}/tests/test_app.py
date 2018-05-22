# -*- coding: utf-8 -*-
""" Test configs """
import unittest

from {{cookiecutter.app_name}} import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app()

    def test_cat_get(self):
        rv = self.app.get('/api/v1')
        import pdb; pdb.set_trace()
        assert b'No entries here so far' in rv.data
