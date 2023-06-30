import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import LabelEncoder

ingredient_list = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime', 'mandarino', 'arancia', 'pompelmo', 'mela', 'banana', 'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']

poke_dataset = np.empty((100, 9), dtype='<U25')
missing_ingredients = []

for i in range(100):
    ingredients = random.sample(ingredient_list, 10)
    missing_ingredient = random.choice(ingredients)
    missing_ingredients.append(missing_ingredient)
    ingredients.remove(missing_ingredient)
    for j in range(9):
        poke_dataset[i][j] = ingredients[j]

le = LabelEncoder()
le.fit(ingredient_list)

poke_dataset_encoded = np.empty((100, 9), dtype=int)
for i in range(100):
    poke_dataset_encoded[i] = le.transform(poke_dataset[i])

missing_ingredients_encoded = le.transform(missing_ingredients)

X_train, X_test, y_train, y_test = train_test_split(poke_dataset_encoded, missing_ingredients_encoded, test_size=0.3, random_state=1)

y_train = y_train.reshape(-1, 1)

forest = RandomForestClassifier(random_state=1)
multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)
multi_target_forest.fit(X_train, y_train)

poke_to_complete = ['avocado', 'mango', 'carote', 'alga nori', 'caviale', 'mela', 'peperoncino', 'aglio', 'prezzemolo']

poke_to_complete_encoded = le.transform(poke_to_complete).reshape(1, -1)
predicted_missing_ingredient_encoded = multi_target_forest.predict(poke_to_complete_encoded)

predicted_missing_ingredient = le.inverse_transform(predicted_missing_ingredient_encoded)[0]

poke_to_complete.append(predicted_missing_ingredient)
print("predicted:"+predicted_missing_ingredient)
print(poke_to_complete)