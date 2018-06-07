from flask import Blueprint

from flask_restplus import Api, Namespace, Resource, fields


blueprint = Blueprint('api', __name__)
api = Api(blueprint)


# we might consider extracting `cat` to models.py or the rest of
# this module into an api_cat namespace
cat = api.model('Cat', {
    'id': fields.String(required=True, description='cat identifier'),
    'name': fields.String(required=True, description='cat name'),
})

CATS = [
    {'id': '1', 'name': 'Furball'},
]

@api.route('/cats')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)
