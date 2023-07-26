#import sys
from flask_cors import CORS
#import os
from flask import Flask, request, send_file
from predict import predictIngredient

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}})
# CORS(app) # <- enables access from all ip


@app.route('/')
def root():
    print('call root')
    #return ('flask api root execute. Nothing to display.')
    return send_file("index.html")


# @app.route("/api/v.1.0/backend_recipe_predict", methods=["GET"])
# def request_get():
#     print("RECEIVED get request")
#     #return (predict.predictIngredient()) # or return(myArray)


@app.route("/api/v.1.0/backend_recipe_predict", methods=["POST"])
def request_post():
    '''
    this is the entry point for web application that calls this post method in order to obtain predictions of ingredients.
    It takes in input the recipe incomplete, for example with 8 ingredients, and it returns 10 ingredients.
    ''' 
    request_data = request.get_json()
    apiPassword = request_data.get("password")
    recipe_incomplete = request_data.get("recipe_incomplete")


    if apiPassword == "Phaser2023":
     
        print("RECEIVED post request")
       

    
        request_data = request.get_json()
        myArray = request_data['recipe_incomplete']

        print('myArray in app.py:', myArray)
        myResult = predictIngredient(recipe_incomplete)
        print('myResult in app.py:', myResult)
        return(myResult)
    else: 
        print("debug: else function")
        print(apiPassword)
        data = [
            'riso bianco', 'salmone crudo', 'tonno crudo', 'daikon', 'zenzero marinato',
            'uovo marinato', 'edamame', 'semi di lino', 'salsa rosa Worcestershire', 'wasabipeas'
        ]
        return(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)