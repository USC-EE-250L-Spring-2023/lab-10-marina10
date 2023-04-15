from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})
   

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.


@app.route('/processs1')
def process1():
    data=request.get.json()
    return jsonify(process1(data))
@app.route('/processs2')
def process2():
    data=request.get.json()
    return jsonify(process2(data))



