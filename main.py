from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    my_set = {"Esto es un mensaje modificado!"}
    return jsonify(list(my_set))

def my_name():
    my_set = {"Hello World my name is: Diego Saavedra"}
    return jsonify(list(my_set))

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))