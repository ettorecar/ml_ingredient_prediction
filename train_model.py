import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import LabelEncoder
from joblib import dump
from sklearn.metrics import classification_report
from constants import *
from sklearn.metrics import accuracy_score
import train_model_inc_plot as trainplot



def creaDataset():
    print('crea dataset')
    # dtype indica che ogni elemento dell'array è una stringa con lunghezza massima di 25 caratteri
    poke_dataset = np.empty(
        (num_row, num_com), dtype='<U25')
    for i in range(num_row):
        # la prossima riga commentata creava dataset completamente casuale
        #poke_dataset[i] = random.sample(list(ingredient_list), num_com)
        # creiamo un dataset con delle associazioni all'interno e un po' di casualità
        group_ingredients = random.sample(ingredient_groups[random.randint(0, len(ingredient_groups)-1)], 6)
        extra_ingredients = random.sample(other_ingredients, 4)
        poke_dataset[i] = group_ingredients + extra_ingredients
    return poke_dataset


def codificaDataset():
    print('codifica dataset')
    poke_dataset = creaDataset()
    le = LabelEncoder()
    le.fit(ingredient_list)  # trasforma gli elementi da testo a numero

    # dtype indica che ogni elemento dell'array è un numero intero
    poke_dataset_encoded = np.empty(
        (num_row, num_com), dtype=int)
    for i in range(num_row):
        # converte ogni singolo elemento in un numero, come previsto dal .fit precedente
        poke_dataset_encoded[i] = le.transform(poke_dataset[i])

    #disegna il grafico
    trainplot.scatter_ingredients(poke_dataset)

    # X è l'input, quindi la matrice delle feature
    X = poke_dataset_encoded[:, :num_inc]
    # y è l'output, comprende le colonne mancanti, cioè le label
    y = poke_dataset_encoded[:, num_inc:]
    return X, y


def calculate_accuracy(multi_target_forest, X_test, y_test):

    le = LabelEncoder()
    le.fit(ingredient_list)
    # calcolo accuratezza media del modello
    y_pred = multi_target_forest.predict(X_test)
    accuracies = []
    for i in range(y_test.shape[1]):
        accuracy = accuracy_score(y_test[:, i], y_pred[:, i])
        accuracies.append(accuracy)

    average_accuracy = sum(accuracies) / len(accuracies)
    print("Average accuracy:", average_accuracy)


def trainTest():
    
    X, y = codificaDataset()

    print('start training model')
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=1)

    # 1: se il dataset di partenza è lo stesso genera sempre gli stessi risultati
    forest = RandomForestClassifier(random_state=1)
    multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)  # -1: utilizza tutti i processori
    multi_target_forest.fit(X_train, y_train)  # addestriamo il modello

    # facciamo delle predizioni sul test set
    predictions = multi_target_forest.predict(X_test)
    # produciamo il report di classificazione
    report = classification_report(y_test, predictions, zero_division=1)

    # stampiamo il report
    print('report: ')
    print(report)

    # altro metodo per calcolare accuracy
    calculate_accuracy(multi_target_forest, X_test, y_test)

    # salva il modello addestrato
    dump(multi_target_forest, 'py_cache/poke_model.joblib')
    print("model saved: py_cache/poke_model.joblib")
    return multi_target_forest

trainTest()

