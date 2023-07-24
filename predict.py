import numpy as np
from sklearn.preprocessing import LabelEncoder
from joblib import load
from constants import *



def loadModel():
    print('load model')
    multi_target_forest = load('py_cache/recipe_model.joblib') #loads the model saved in joblib file
    return multi_target_forest

def predictIngredient(myArray):
    print(recipe_incomplete)
    print('predict ingredient')

    le = LabelEncoder()
    le.fit(ingredient_list)


    multi_target_forest = loadModel()
    recipe_incomplete_incomplete_encoded = multi_target_forest.estimators_[0].classes_  #takes classes as codified in model
    num_inc = len(myArray) #reads array's lenght
    recipe_incomplete_incomplete_encoded = le.transform(myArray[:num_inc]).reshape(1, -1) #reshape(1, -1) returns an array with a single row, with num of columns determined in transform() 
    predicted_missing_ingredients_encoded = multi_target_forest.predict(recipe_incomplete_incomplete_encoded) #after fit, inavitable predict for the prediction
    print (predicted_missing_ingredients_encoded)
    for ingredient_encoded in predicted_missing_ingredients_encoded:
        predicted_ingredient = le.inverse_transform(ingredient_encoded)
        print(predicted_ingredient)
    
    predicted_probabilities = multi_target_forest.predict_proba(recipe_incomplete_incomplete_encoded) #indicates prediction's probability 
        #print (predicted_probabilities)
    missing_ingredients_count = num_com - num_inc
    #predicted_ingredients = []

    # cycles through results for each label
    counter = 1

    for label_probs in predicted_probabilities:
        # obtain max probability
        max_probability = label_probs.max()
        
        # prints max probability for current label
        print("Ma probability for label", counter, "is:", str(max_probability*100)+"%")
        counter += 1



    myArray.extend(predicted_ingredient)
    print(myArray)
    
    return(myArray)
 
predictIngredient(recipe_incomplete) 