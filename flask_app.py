from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/get_current_temp')
def get_current_temp():
    #TODO return actual values
    return jsonify({"sensor1": 23, "sensor2": 24})

#
# @app.route('/add_sensor')
# def add_sensor():
#
