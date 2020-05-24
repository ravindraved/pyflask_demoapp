from flask import Flask

app = Flas(__name__)


# post /store data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    pass


# post /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# Get /store
@app.route('/store')
def get_stores():
    pass


# Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store():
    pass


# GEt /store/<string:name>/item
@app.route('/store/<string:store_name>/item')
def get_items_in_store(store_name):
    pass

app.run(port=5001)
