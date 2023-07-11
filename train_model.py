import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import LabelEncoder
from joblib import dump
from sklearn.metrics import classification_report
from constants import *


def creaDataset():
    print('crea dataset')
    poke_dataset = np.empty((num_el_dataset_training, num_el_complete), dtype='<U25') #dtype indica che ogni elemento dell'array è una stringa con lunghezza massima di 25 caratteri
    for i in range(num_el_dataset_training):
        poke_dataset[i] = random.sample(list(ingredient_list), num_el_complete) #usato list invece di set, perchè deprecato
    return poke_dataset


def codificaDataset():
    print('codifica dataset')
    poke_dataset = creaDataset()
    le = LabelEncoder()
    le.fit(ingredient_list)  #trasforma gli elementi da testo a numero

    poke_dataset_encoded = np.empty((num_el_dataset_training, num_el_complete), dtype=int) #dtype indica che ogni elemento dell'array è un numero intero
    for i in range(300):
        poke_dataset_encoded[i] = le.transform(poke_dataset[i]) #converte ogni singolo elemento in un numero, come previsto dal .fit precedente

    X = poke_dataset_encoded[:, :num_el_incomplete] #X è l'input, quindi la matrice delle feature
    y = poke_dataset_encoded[:, num_el_incomplete:] #y è l'output, comprende le colonne mancanti, cioè le label
    return X, y, le

# def is_float(val): ***SERVE PER STAMPARE QUATTRO CIFRE DECIMALI NEL REPORT***
#         try:
#             float(val)
#             return True
#         except ValueError:
#             return False
        
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
    # for line in report.split('\n'): ***SERVE PER STAMPARE QUATTRO CIFRE DECIMALI NEL REPORT***
    #     newline = ' '.join(["{:.4f}".format(float(val)) if is_float(val) else val for val in line.split()])
    #     print(newline)

    dump(multi_target_forest, 'py_cache/poke_model.joblib') #salva il modello addestrato


    return multi_target_forest

trainTest()

#1 nel file ingredients_lists spostare anche le costanti numeriche. p.s. casomai rinominare il file in constants.py, cambiare anche l'import importando tutto (*). ***FATTO***
#2 spostare la funzione accuracy nel file train e cancellare i file cache se non servono più ***LASCIATA COMMENTATA***
#3 verificare se si può cambiare nel metodo che stampa le "statistiche" i numeri decimali (invece di 2 qualcuno in più) in modo da capire che la funzione che calcula l'accuracy a mano sia superflua ***LASCIATI I COMANDI COMMENTATI, STAMPANO DUE ZERI EXTRA PER ARRIVARE A QUATTRO CIFRE DECIMALI***
#4 esporre il metodo predict ingredient in get (inizialmente poi lo metteremo in post), in modo da lanciare il file app (rimane attivo), e provare a chiamare le funzioni inserendo l'indirizzo da una pagina web ***FATTO***
#4bis cambiare il return di predict facendo restituire solo quello che dobbiamo stampare in pagina ***FATTO***
#5 quando faremo il metodo post (copiare dall'altro progetto AI generativa) creiamo una pagina web in cui viene effettuata una chiamata post e gli passiamo gli ingredienti in input al metodo esposto e passato in input al metodo predict
#6 [inizia a vedere ettore] se possibile creare un modello sempre random ma con qualche associazione intrinseca all'interno

