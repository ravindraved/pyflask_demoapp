from flask import Flask, request, jsonify

app = Flask(__name__)

stores = [

    {
        'name': 'store_1',
        'items':
            [
                {'name': 'store_1_item_1',
                 'price': 15.99,
                 'available_qty': 12},
                {
                    'name': 'store_1_item_2',
                    'price': 12.99
                }
            ]

    },

    {
        'name': 'store_2',
        'items': [
            {'name': 'store_2_item_1',
             'price': 15.99,
             'available_qty': 12
             },

            {'name': 'store_2_item_2',
             'price': 12.99,
             'available_qty': 12
             }
            ,

            {'name': 'store_2_item_3',
             'price': 12.99,
             'available_qty': 12
             }
        ]

    }

]


# post /store data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()

    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify("store_added", new_store)


# post /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    # Convert received JSON String into Python Dictionay
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# Get /store
@app.route('/store')
def get_stores():
    # return stores -> raise TypeError : The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list.

    return jsonify('stores:', stores)


# Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GEt /store/<string:name>/item
@app.route('/store/<string:store_name>/item')
def get_items_in_store(store_name):
    for store in stores:
        if store['name'] == store_name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5001)
