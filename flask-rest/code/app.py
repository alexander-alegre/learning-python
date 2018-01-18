from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []
successMessage = { 'code': 200, 'message': 'Success' }
errorMessage = { 'code': 404, 'message': 'Item not found' }

class Item(Resource):
    # return an item by name
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return errorMessage

    # create an item with a name
    def post(self, name):
        item = { 'name': name, 'price': 12.00 }
        items.append(item)
        return successMessage

api.add_resource(Item, '/item/<string:name>')


class Items(Resource):
    # retrieve all items 
    def get(self):
        return items

api.add_resource(Items, '/items')


app.run(port=5000)