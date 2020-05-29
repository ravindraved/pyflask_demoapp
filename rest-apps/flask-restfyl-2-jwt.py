from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

"""
check u are in right env - conda env list => pflask
pip install flask, flask-restful , flask-jwt, 
"""

"""
what is jwt -> obfuscation of data .. encoding some data .. that's JWT.!
user send credentials.. and once we authentice that .. we send them JWT .. that's can be userid....so next time they just send us this token and we know that they were previously authenticated by us so they are logged in !

to encrypt data ..required by jwt obfcustin .. u need secret_key

"""
app = Flask(__name__)
app.secret_key = 'sec_key_random_here'
api = Api(app)

# using flask_jwt package, and we created two methods authenticate and identity in security module.
jwt = JWT(app, authenticate, identity)
# flask auto creates and /auth endpoint for us whic requres username and password that is then used to create JWT token

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": f"an item with name {name} already exist"}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        print(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}

    def put(self, name):

        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type=float,
                            required=True,
                            help="This field cannot be empty"
                            )

        #data = request.get_json()
        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        print("item->", item)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            print("data->", data)
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5010, debug=True)
