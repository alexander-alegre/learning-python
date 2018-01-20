import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )

    @jwt_required()  # this will make it so the request requires authentication
    def get(self, name):
        connection = sqlite = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[1], 'price': row[2]}}

        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'An item with name "{}" already exists.'.format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return successMessage, 201

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted: "{}"'.format(name)}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class Items(Resource):
    # retrieve all items
    @jwt_required()
    def get(self):
        return items, 200
