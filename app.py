import sys
from flask_cors import CORS
import os
from flask import Flask, request, Response

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})
# CORS(app) # <-sblocca gli accessi da tutti gli ip



@app.route('/')
def root():
    print('call root')
    return ('flask api root execute. Nothing to display.')


# @app.route('/mariarosaria')
# def mr():
#     print('call maria rosaria')
#     ingredient_list = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime', 'mandarino', 'arancia', 'pompelmo', 'mela', 'banana', 'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']

#     return ""+str(ingredient_list) 


@app.route("/api/v.1.0/backend_poke_predict", methods=["GET"])
def request_get():
    print("RECEIVED get request")
    return ("get request not allowed")


@app.route("/api/v.1.0/backend_poke_predict", methods=["POST"])
def request_post():
    print("RECEIVED post request")
    return ("ok")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
