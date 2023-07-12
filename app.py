import sys
from flask_cors import CORS
import os
from flask import Flask, request, Response
import predict_more

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}})
# CORS(app) # <-sblocca gli accessi da tutti gli ip



@app.route('/')
def root():
    print('call root')
    return ('flask api root execute. Nothing to display.')


@app.route("/api/v.1.0/backend_poke_predict", methods=["GET"])
def request_get():
    print("RECEIVED get request")
    return (predict_more.predictIngredient())
    # da sostituire con il return del metodo predict


@app.route("/api/v.1.0/backend_poke_predict", methods=["POST"])
def request_post():
    print("RECEIVED post request")
    # return('stringa')
   
    request_data = request.get_json()
    myArray = request_data['poke_incomplete']
    # return("ok")

    print("ciao")
    print(myArray)
    myArray = myArray.split(", ")
    myResult = predict_more.predictIngredient(myArray)
    print('casa')
    print(myResult)
    return(myResult)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
