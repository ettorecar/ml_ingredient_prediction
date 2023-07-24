import sys
from flask_cors import CORS
import os
from flask import Flask, request
import requests
# from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}})
# CORS(app) # <- enables access from all ip


# @app.route('/')
# def root():
#     print('call root')
#     return ('flask api root execute. Nothing to display.')


# @app.route("/api/v.1.0/backend_recipe_predict", methods=["GET"])
# def request_get():
#     print("RECEIVED get request")
#     #return (predict.predictIngredient()) # or return(myArray)


@app.route("/api/v.1.0/backend_recipe_predict", methods=["POST"])
def request_post():
     
    request_data = request.get_json()
    apiPassword = request_data.get("password")
    recipe_incomplete = request_data.get("recipe_incomplete")
    # apiPassword = request.form.get("password")

    # url = "http://127.0.0.1:5500/index.html"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html.parser")
    # apiPassword = soup.find("meta", {"name": "password"})["content"]

    if apiPassword == "Phaser2023":
     
        print("RECEIVED post request")
        from predict import predictIngredient

    
        request_data = request.get_json()
        myArray = request_data['recipe_incomplete']

        print(myArray)
        myResult = predictIngredient(recipe_incomplete)
        print(myResult)
        return(myResult)
    else: 
        print("sono nell'else")
        print(apiPassword)
        data = [
            'riso bianco', 'salmone crudo', 'tonno crudo', 'daikon', 'zenzero marinato',
            'uovo marinato', 'edamame', 'semi di lino', 'salsa rosa Worcestershire', 'wasabipeas'
        ]
        return(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)