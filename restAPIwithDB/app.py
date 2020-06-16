from flask import Flask, jsonify, request
import dbmodule

app = Flask(__name__)

@app.route('/register', methods = ['POST'])
def register():
    inp = request.get_json()
    out = dbmodule.insert(inp["id_"],inp["pass_"],inp["phone_"])
    return jsonify({'message': out})

@app.route('/updpassword', methods = ['POST'])
def upd_password():
    inp = request.get_json()
    out = dbmodule.update_password(inp["id_"], inp["pass_"])
    return jsonify({'message': out})

@app.route('/login/<string:userid>/<string:password>')
def login(userid,password):
    res = dbmodule.select(userid,password)
    if len(res)>0:
        return jsonify('Login Successful')
    else:
        return jsonify('Login Failed')

app.run()