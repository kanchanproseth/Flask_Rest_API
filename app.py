from flask import Flask, jsonify, request
from flask_restful import Api
from flask_restful_swagger import swagger

app = Flask(__name__)
store = [
    {
        'name': 'Sovanna Supper Market',
        'item': [
            {
                'name': 'prime ticket',
                'price': 3
            }
        ]
    },
    {
        'name': 'Soriya Supper Market',
        'item': [
            {
                'name': 'Major ticket',
                'price': 3
            }
        ]
    },
    {
        'name': 'TK Supper Market',
        'item': [
            {
                'name': 'Legend ticket',
                'price': 3
            }
        ]
    },
    {
        'name': 'Mean Jey Supper Market',
        'item': [
            {
                'name': 'Legend ticket',
                'price': 3
            }
        ]
    }
]

# POST /store data: {name:}


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    store.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>


@app.route('/store/<string:name>')
def get_store_by_name(name):
    for each_store in store:
        if each_store['name'] == name:
            return jsonify(each_store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_store():
    return jsonify({'store': store})

# POST /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for each_store in store:
        if each_store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            each_store['item'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for each_store in store:
        if each_store['name'] == name:
            return jsonify({'items': each_store['item']})
    return jsonify({'message': 'store not found'})


@app.route('/')
#http://www.google.com/
def home():
    return "Welcome Home"


app.run(port=5000)