from flask_restplus import Namespace, Resource, fields


api = Namespace('cats', description='Cats related operations')


cat = api.model('Cat', {
    'id': fields.String(required=True, description='cat identifier'),
    'name': fields.String(required=True, description='cat name'),
})


# Practically, we'd probably use sqlalchemy here. Keeping scope
# small for flexibility with other things - dynamodb e.g. *shrugs*
CATS = [
    {'id': '1', 'name': 'Furball'},
]


@api.route('/')
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
