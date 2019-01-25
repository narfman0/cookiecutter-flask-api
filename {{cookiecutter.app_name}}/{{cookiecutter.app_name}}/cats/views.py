from flask_restplus import Resource

from {{cookiecutter.app_name}}.cats import controller, models
from {{cookiecutter.app_name}}.cats.api import api


@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(models.cat)
    def get(self):
        '''List all cats'''
        return controller.list_cats()


@api.route('/<id>/')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(models.cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        return controller.get_cat(id)
