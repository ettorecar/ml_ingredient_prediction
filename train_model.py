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



def createDataset():
    print('Create Dataset')
    # dtype indica che ogni elemento dell'array è una stringa con lunghezza massima di 25 caratteri
    poke_dataset = np.empty((num_row, num_com), dtype='<U25')
    for i in range(num_row):
        poke_dataset[i] = random.sample(ing_basi, 1) +  random.sample(ing_princ, 2) + random.sample(ing_altri, 4) + random.sample(ing_semi, 1) + random.sample(ing_salsa, 1) + random.sample(ing_topping, 1) 
  
    #print (poke_dataset)
    return poke_dataset


def encodeDataset():
    print('Encode Dataset')
    poke_dataset = createDataset()
    le = LabelEncoder()
    le.fit(ingredient_list)  # trasforma gli elementi da testo a numero
    encoded_list = le.transform(ingredient_list)

    # stampa ingrediente e id numerico assegnato 
    for ingredient, number in zip(ingredient_list, encoded_list):
        print(f"Inggredient: {ingredient} | Id encod: {number}")

    poke_dataset_encoded = np.empty( (num_row, num_com), dtype=int)
    for i in range(num_row):
        # converte ogni singolo elemento in un numero, come previsto dal .fit precedente
        poke_dataset_encoded[i] = le.transform(poke_dataset[i])


    #conteggia quante volte appaiono gli ingredienti nel dataset in totale per ingrediente
    #unique_numbers, counts = np.unique(poke_dataset, return_counts=True)
    #for number, count in zip(unique_numbers, counts):
    #    print(f"{number}: {count}")
    #print (poke_dataset_encoded)

    #disegna il grafico a dispersione degli ingredienti
    trainplot.scatter_ingredients(poke_dataset)

    return poke_dataset_encoded


def calculateAccuracy(multi_target_forest, X_test, y_test):
    le = LabelEncoder()
    le.fit(ingredient_list)
    # calcolo accuratezza media del modello
    y_pred = multi_target_forest.predict(X_test)
    accuracies = []
    for i in range(y_test.shape[1]):
        accuracy = accuracy_score(y_test[:, i], y_pred[:, i])
        accuracies.append(accuracy)

    average_accuracy = sum(accuracies) / len(accuracies)
    print("Average Accuracy:", average_accuracy)


def trainTest():

    poke_dataset_encoded = encodeDataset()

    # X è l'input, quindi la matrice delle feature
    X = poke_dataset_encoded[:, :num_inc]
    # y è l'output, comprende le colonne mancanti, cioè le label
    y = poke_dataset_encoded[:, num_inc:]

    print('*** Start Training Model... ... ***')
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=1)

    # 1: se il dataset di partenza è lo stesso genera sempre gli stessi risultati
    forest = RandomForestClassifier(random_state=1)
    multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)  # -1: utilizza tutti i processori
    multi_target_forest.fit(X_train, y_train)  # addestriamo il modello

    #grafico dell'importanza delle feature, sembra funzionare a caso
    #trainplot.plotFeatures(multi_target_forest, X_train, y_train)

    # facciamo delle predizioni sul test set
    predictions = multi_target_forest.predict(X_test)
    #print ('predictions:')
    #print (predictions)
    
    # Produci il report di classificazione per la prima etichetta
    report_label1 = classification_report(y_test[:, 0], predictions[:, 0], zero_division=1)
    print("Report first label:\n", report_label1)

    # Produci il report di classificazione per la seconda etichetta
    report_label2 = classification_report(y_test[:, 1], predictions[:, 1], zero_division=1)
    print("Report second label:\n", report_label2)

    # Calcola la matrice di correlazione
    correlation_matrix = np.corrcoef(predictions, rowvar=False)

    # Stampa la matrice di correlazione
    print("Correlation Matrix:\n", correlation_matrix)


    # stampiamo il report (funziona solo quando c'è una label da fittare, siamo passati a 2 ora)
    #print('report: ')
    #print(report)

    # altro metodo per calcolare accuracy
    calculateAccuracy(multi_target_forest, X_test, y_test)

    # salva il modello addestrato
    dump(multi_target_forest, 'py_cache/poke_model.joblib')
    print("model saved: py_cache/poke_model.joblib")
    return multi_target_forest

trainTest()