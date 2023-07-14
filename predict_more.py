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

    le = LabelEncoder()
    le.fit(ingredient_list)


    multi_target_forest = loadModel()
    poke_incomplete_encoded = multi_target_forest.estimators_[0].classes_  #Riprende le classi così come codificate nel modello
    num_inc = len(poke_incomplete) #legge la lunghezza dell'array
    poke_incomplete_encoded = le.transform(poke_incomplete[:num_inc]).reshape(1, -1) #reshape(1, -1) resituisce un array con una singola riga, con il numero di colonne determinato dal transform()
    predicted_missing_ingredients_encoded = multi_target_forest.predict(poke_incomplete_encoded) #dopo il fit, immancabile il predict per fare la predizione
    print (predicted_missing_ingredients_encoded)
    for ingredient_encoded in predicted_missing_ingredients_encoded:
        predicted_ingredient = le.inverse_transform(ingredient_encoded)
        print(predicted_ingredient)
    
    predicted_probabilities = multi_target_forest.predict_proba(poke_incomplete_encoded) #indica la probabilità della predizione
    #print (predicted_probabilities)
    missing_ingredients_count = num_com - num_inc
    #predicted_ingredients = []

    # Cicla attraverso i risultati per ogni label
    counter = 1

    # Cicla attraverso i risultati per ogni label
    for label_probs in predicted_probabilities:
        # Ottieni la probabilità più alta
        max_probability = label_probs.max()
        
        # Stampa la probabilità più alta per la label corrente
        print("La probabilità più alta per la label", counter, "è:", str(max_probability*100)+"%")
        counter += 1



    poke_incomplete.extend(predicted_ingredient)
    print(poke_incomplete)
    
    return(poke_incomplete)
 
predictIngredient(poke_incomplete) 