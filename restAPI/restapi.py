from flask import Flask

app = Flask(__name__)
@app.route('/func')
def func():
    return 'Hello World'

#func()

@app.route('/bye')
def bye():
    return 'bye bye'
#port 5000-6000 are available for public
app.run(port=5000)