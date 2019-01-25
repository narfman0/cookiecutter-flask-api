from flask_restplus import fields

from {{cookiecutter.app_name}}.cats.api import api

cat = api.model('Cat', {
    'id': fields.String(required=True, description='cat identifier'),
    'name': fields.String(required=True, description='cat name'),
})
