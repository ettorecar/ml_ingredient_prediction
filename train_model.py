import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import LabelEncoder
from joblib import dump
from sklearn.metrics import classification_report


#ingredient_list_short = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime']
ingredient_list = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime', 'mandarino', 'arancia', 'pompelmo', 'mela', 'banana', 'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']

num_el_incomplete = 9 #lunghezza dell'array esclusi gli ingredienti mancanti
num_el_complete = 10 #lunghezza dell'array compresi gli ingredienti mancanti

def creaDataset():
    print('crea dataset')
    poke_dataset = np.empty((300, num_el_complete), dtype='<U25') #dtype indica che ogni elemento dell'array è una stringa con lunghezza massima di 25 caratteri
    for i in range(300):
        poke_dataset[i] = random.sample(list(ingredient_list), num_el_complete) #usato list invece di set, perchè deprecato
    return poke_dataset


def codificaDataset():
    print('codifica dataset')
    poke_dataset = creaDataset()
    le = LabelEncoder()
    le.fit(ingredient_list)  #trasforma gli elementi da testo a numero

    poke_dataset_encoded = np.empty((300, num_el_complete), dtype=int) #dtype indica che ogni elemento dell'array è un numero intero
    for i in range(300):
        poke_dataset_encoded[i] = le.transform(poke_dataset[i]) #converte ogni singolo elemento in un numero, come previsto dal .fit precedente

    X = poke_dataset_encoded[:, :num_el_incomplete] #X è l'input, quindi la matrice delle feature
    y = poke_dataset_encoded[:, num_el_incomplete:] #y è l'output, comprende le colonne mancanti, cioè le label
    return X, y, le


def trainTest():
    print('train test')
    X, y, le = codificaDataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    np.save("py_cache/X_train.npy", X_train) #salva i risultati per calcolare poi l'accuratezza
    np.save("py_cache/X_test.npy", X_test)
    np.save("py_cache/y_train.npy", y_train)
    np.save("py_cache/y_test.npy", y_test)
    
    forest = RandomForestClassifier(random_state=1) #1: se il dataset di partenza è lo stesso genera sempre gli stessi risultati
    multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1) #-1: utilizza tutti i processori
    multi_target_forest.fit(X_train, y_train) #addestriamo il modello

    # facciamo delle predizioni sul test set
    predictions = multi_target_forest.predict(X_test)

    # produciamo il report di classificazione
    report = classification_report(y_test, predictions)

    # stampiamo il report
    print('report: ')
    print(report)

    dump(multi_target_forest, 'py_cache/poke_model.joblib') #salva il modello addestrato

    return multi_target_forest

trainTest()
