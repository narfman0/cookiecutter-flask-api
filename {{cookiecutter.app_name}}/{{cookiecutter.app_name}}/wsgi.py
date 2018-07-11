# -*- coding: utf-8 -*-
"""The wsgi module, helpful for serverless-wsgi."""
from {{ cookiecutter.app_name }}.app import create_app


app = create_app()
