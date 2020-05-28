from flask import Flask, request
from flask_restful import Resource, Api

"""
check u are in right env - conda env list => pflask
pip install flask, flask-restful , flask-jwt, 
"""

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    @staticmethod
    def get(name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404

    @staticmethod
    def post(name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": f"an item with name {name} already exist"}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        print(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5010, debug=True)
