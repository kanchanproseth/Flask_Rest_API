from flask import Flask, jsonify

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
@app.route('/store', methods = ['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store_by_name(name):
    pass

# GET /store
@app.route('/store')
def get_store():
    return jsonify({'store': store})

# POST /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

@app.route('/')
#http://www.google.com/ 

def home():
    return "Welcome Home"

app.run(port=5000)