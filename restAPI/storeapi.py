from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'DMart',
        'items':[{'name': 'Chair','price': 900}]
    },
{
        'name':'RMart',
        'items':[]
    }
,
{
        'name':'N Mart',
        'items':[]
    }
]
@app.route('/getallstores')
def getall():
    return jsonify({'output':stores})

@app.route('/addstore', methods=['POST'])
def addstore():
    store_data = request.get_json()
    for store in stores:
        if store['name'] == store_data['name']:
            return jsonify({'message':'Store Already Exists'})
    stores.append(store_data)
    return jsonify({'message': 'Store Added'})


@app.route('/findstore/<string:store_name>')
def searchstore(store_name):
    for store in stores:
        if store['name'] == store_name:
            return jsonify(store)
    return jsonify({'Message':'Store not found in records.'})

@app.route('/additem/<string:store_name>', methods = ['POST'])
def additem(store_name):
    item_data = request.get_json()
    for store in stores:
        if store['name'] == store_name:
            #store['items'].append(item_data)
            #return jsonify({'Message': 'Item Added..!!!'})
            for item in store['items']:
                if item['name'] == item_data['name']:
                    return jsonify({'Message':'Item Already Exists'})
            store['items'].append(item_data)
            return jsonify({'Message':'Item Added..!!!'})
    return jsonify({'Message':'Store not found in records, could not add item'})

@app.route('/additemnew', methods = ['POST'])
def additemnew():
    input_data = request.get_json()
    store_name = input_data['storename']
    item_data = input_data['item_data']
    for store in stores:
        if store['name'] == store_name:
            #store['items'].append(item_data)
            #return jsonify({'Message': 'Item Added..!!!'})
            for item in store['items']:
                if item['name'] == item_data['name']:
                    return jsonify({'Message':'Item Already Exists'})
            store['items'].append(item_data)
            return jsonify({'Message':'Item Added..!!!'})
    return jsonify({'Message':'Store not found in records, could not add item'})

app.run(port=5000)