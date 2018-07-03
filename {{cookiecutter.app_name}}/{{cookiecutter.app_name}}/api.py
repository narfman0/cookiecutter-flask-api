from flask import Blueprint

from flask_restplus import Api

from {{ cookiecutter.app_name }}.cats import api as ns_cats


blueprint = Blueprint('api', __name__)
api = Api(blueprint)
api.add_namespace(ns_cats)
