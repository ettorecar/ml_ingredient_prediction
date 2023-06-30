import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import LabelEncoder

#ingredient_list_short = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime']
ingredient_list = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime', 'mandarino', 'arancia', 'pompelmo', 'mela', 'banana', 'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']

poke_incomplete = ['lattuga', 'salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale']
num_el_incomplete = len(poke_incomplete)

poke_dataset = np.empty((100, 10), dtype='<U25')
for i in range(100):
    poke_dataset[i] = random.sample(list(ingredient_list), 10) #usato list invece di set, perchè deprecato

le = LabelEncoder()
le.fit(ingredient_list)  #trasforma gli elementi da testo a numero

poke_dataset_encoded = np.empty((100, 10), dtype=int)
for i in range(100):
    poke_dataset_encoded[i] = le.transform(poke_dataset[i]) #converte ogni singolo elemento in un numero, come previsto dal .fit precedente

X = poke_dataset_encoded[:, :num_el_incomplete] #X è l'input, quindi la matrice delle feature
y = poke_dataset_encoded[:, num_el_incomplete:] #y è l'output, comprende le colonne mancanti, cioè le label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

forest = RandomForestClassifier(random_state=1) #1: se il dataset di partenza è lo stesso genera sempre gli stessi risultati
multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1) #-1: utilizza tutti i processori
multi_target_forest.fit(X_train, y_train) #addestriamo il modello

poke_incomplete_encoded = le.transform(poke_incomplete[:num_el_incomplete]).reshape(1, -1)
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


def calculate_accuracy():
    #calcolo accuratezza media del modello
    from sklearn.metrics import accuracy_score
    y_pred = multi_target_forest.predict(X_test)
    accuracies = []
    for i in range(y_test.shape[1]):
        accuracy = accuracy_score(y_test[:, i], y_pred[:, i])
        accuracies.append(accuracy)

    average_accuracy = sum(accuracies) / len(accuracies)
    print("Average accuracy:", average_accuracy)

calculate_accuracy()