import numpy as np
from sklearn.preprocessing import LabelEncoder
from joblib import load
from constants import *


def loadModel():
    print('load model')
    multi_target_forest = load('py_cache/poke_model.joblib') #carica il modello dal file joblib salvato
    return multi_target_forest

def predictIngredient(myArray):
    print('predict ingredient')

    # poke_incomplete = myArray.split(", ")
    le = LabelEncoder()
    le.fit(ingredient_list)

    multi_target_forest = loadModel()
    poke_incomplete_encoded = multi_target_forest.estimators_[0].classes_  #Riprende le classi così come codificate nel modello
    num_el_incomplete = len(poke_incomplete) #legge la lunghezza dell'array
    poke_incomplete_encoded = le.transform(poke_incomplete[:num_el_incomplete]).reshape(1, -1) #reshape(1, -1) resituisce un array con una singola riga, con il numero di colonne determinato dal transform()
    predicted_missing_ingredients_encoded = multi_target_forest.predict(poke_incomplete_encoded) #dopo il fit, immancabile il predict per fare la predizione
    predicted_probabilities = multi_target_forest.predict_proba(poke_incomplete_encoded) #indica la probabilità della predizione

    missing_ingredients_count = num_el_complete - num_el_incomplete
    predicted_ingredients = []

    for _ in range(missing_ingredients_count):
        max_prob = 0
        max_prob_ingredient = ''
        for prob_array in predicted_probabilities:
            max_prob_current = np.max(prob_array)
            max_prob_index = np.argmax(prob_array)
            current_ingredient = ingredient_list[max_prob_index]
            if max_prob_current > max_prob and current_ingredient not in poke_incomplete and current_ingredient not in predicted_ingredients:
                max_prob = max_prob_current
                max_prob_ingredient = current_ingredient
        predicted_ingredients.append(max_prob_ingredient)
        probability = max_prob * 100
        print("predicted:", max_prob_ingredient, "with probability:", probability, "%")

    poke_incomplete.extend(predicted_ingredients)
    print(poke_incomplete)
    
    return(poke_incomplete)

#***SE ATTIVO NEL GET DI APP.PY QUI NON SERVE. FAREBBE PARTIRE PRIMA LA FUNZIONE E CERCHEREBBE DI PREDIRE DI NUOVO CON 10 INGREDIENTI GIà NELL'ARRAY***
# predictIngredient(poke_incomplete) 