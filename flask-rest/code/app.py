from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []
successMessage = { 'code': 200, 'message': 'Success' }
errorMessage = { 'code': 404, 'message': 'Item not found' }

class Item(Resource):
    # return an item by name
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return { 'item': item }, 200 if item else 404

    # create an item with a name
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return { 'message': 'An item with name "{}" already exists.'.format(name) }, 400


        data = request.get_json()
        item = { 'name': name, 'price': data['price'] }
        items.append(item)
        return successMessage, 201

api.add_resource(Item, '/item/<string:name>')


class Items(Resource):
    # retrieve all items 
    def get(self):
        return items, 200

api.add_resource(Items, '/items')


app.run(port=5000, debug=True)