import numpy as np
from sklearn.preprocessing import LabelEncoder
from joblib import load
from sklearn.metrics import accuracy_score
from ingredients_lists import poke_incomplete, poke_incomplete_alt, ingredient_list_short, ingredient_list


def loadModel():
    print('load model')
    multi_target_forest = load('py_cache/poke_model.joblib') #carica il modello dal file joblib salvato
    return multi_target_forest

def predictIngredient():
    print('predict ingredient')

    le = LabelEncoder()
    le.fit(ingredient_list)

    multi_target_forest = loadModel()
    poke_incomplete_encoded = multi_target_forest.estimators_[0].classes_  #Riprende le classi così come codificate nel modello
    num_el_incomplete = len(poke_incomplete) #legge la lunghezza dell'array
    poke_incomplete_encoded = le.transform(poke_incomplete[:num_el_incomplete]).reshape(1, -1) #reshape(1, -1) resituisce un array con una singola riga, con il numero di colonne determinato dal transform()
    predicted_missing_ingredients_encoded = multi_target_forest.predict(poke_incomplete_encoded) #dopo il fit, immancabile il predict per fare la predizione
    predicted_probabilities = multi_target_forest.predict_proba(poke_incomplete_encoded) #indica la probabilità della predizione

    missing_ingredients_count = 10 - num_el_incomplete
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
    
    return multi_target_forest, poke_incomplete_encoded, predicted_missing_ingredients_encoded
    #forse nel return non dovremo restituire tutto ma solo l'array con gli ingredienti completo


predictIngredient()

'''
def calculate_accuracy():
    print('calculate accuracy')




    X_train = np.load("py_cache/X_train.npy") #recupera i risultati salvati in train_model
    X_test = np.load("py_cache/X_test.npy")
    y_train = np.load("py_cache/y_train.npy")
    y_test = np.load("py_cache/y_test.npy")

    #calcolo accuratezza media del modello   
    y_pred = multi_target_forest.predict(X_test)
    accuracies = []
    for i in range(y_test.shape[1]):
        accuracy = accuracy_score(y_test[:, i], y_pred[:, i])
        accuracies.append(accuracy)

    average_accuracy = sum(accuracies) / len(accuracies)
    print("Average accuracy:", average_accuracy)

calculate_accuracy()

'''