from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    @staticmethod
    def get(name):
        for item in items:
            print(item)
            if item['name'] == name:
                return item
        return {'item': None}, 404

    @staticmethod
    def post(name):
        # force=True will set content/Type to JSON .. silent=True will return None
        data = request.get_json(force=True)
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
