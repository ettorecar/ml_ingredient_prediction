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
    '''
    since we do not have a real dataset, for testing purposes we build a list of recipes with random ingredients, 
    taking pokes as a reference, we create bowls with the correct number of ingredients by type
    ''' 
    print('Create Dataset')
    # dtype means that each array's element is a string with max lenght of 25 characters 
    recipe_dataset = np.empty((num_row, num_com), dtype='<U25')
    for i in range(num_row):
        recipe_dataset[i] = random.sample(ing_bases, 1) +  random.sample(ing_princ, 2) + random.sample(ing_others, 4) + random.sample(ing_seeds, 1) + random.sample(ing_sauce, 1) + random.sample(ing_topping, 1) 
    
    return recipe_dataset


def encodeDataset():
    '''
    the dataset is converted from string to number in order to facilitate the ML operations
    '''
    recipe_dataset = createDataset()
    le = LabelEncoder()
    le.fit(ingredient_list) 
    encoded_list = le.transform(ingredient_list)

    # prints ingredient and numeric id assigned 
    for ingredient, number in zip(ingredient_list, encoded_list):
        print(f"Ingredient: {ingredient} | Id encod: {number}")

    recipe_dataset_encoded = np.empty( (num_row, num_com), dtype=int)
    for i in range(num_row):

        recipe_dataset_encoded[i] = le.transform(recipe_dataset[i])


    #counts the total times ingredients appear in dataset, for each ingredient
    #unique_numbers, counts = np.unique(recipe_dataset, return_counts=True)
    #for number, count in zip(unique_numbers, counts):
    #    print(f"{number}: {count}")
    #print (recipe_dataset_encoded)

    # print dataset shape
    print("Dataset shape:")
    print(recipe_dataset.shape)
    

    #draws the ingredients' scatter plot 
    trainplot.scatter_ingredients(recipe_dataset)

    return recipe_dataset_encoded


def calculateAccuracy(multi_target_forest, X_test, y_test):
    '''
    It calculates the average accuracy of the model
    '''
    le = LabelEncoder()
    le.fit(ingredient_list)
    y_pred = multi_target_forest.predict(X_test)
    accuracies = []
    for i in range(y_test.shape[1]):
        accuracy = accuracy_score(y_test[:, i], y_pred[:, i])
        accuracies.append(accuracy)

    average_accuracy = sum(accuracies) / len(accuracies)
    print("Average Accuracy:", average_accuracy)


def trainTest():
    '''
    main method of training step.
    It use the Random Forest Classifier as model.
    Also in this method we print reports and other useful data for debug and also to validate the model

    '''

    recipe_dataset_encoded = encodeDataset()

    # X is the input (feature matrix)
    X = recipe_dataset_encoded[:, :num_inc]
    # y is the output (missing colums = label)
    y = recipe_dataset_encoded[:, num_inc:]

    print('*** Start Training Model... ... ***')
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=1)

    # random_state= 1: if the starting dataset is the same, it generates always same results
    forest = RandomForestClassifier(random_state=1)
    multi_target_forest = MultiOutputClassifier(forest, n_jobs=4)  # -1: uses all precessors but it doesn't work on pythonanywhere
    multi_target_forest.fit(X_train, y_train)  # train the model

    # features importance's plot, seems like it works randomly
    #trainplot.plotFeatures(multi_target_forest, X_train, y_train)

    # predictions based on test set
    predictions = multi_target_forest.predict(X_test)
    #print ('predictions:')
    #print (predictions)
    
    # princes the classification report for the first label 
    report_label1 = classification_report(y_test[:, 0], predictions[:, 0], zero_division=1)
    print("Report first label:\n", report_label1)

    # princes the classification report for the second label 
    report_label2 = classification_report(y_test[:, 1], predictions[:, 1], zero_division=1)
    print("Report second label:\n", report_label2)

    # calculate the correlation matrix
    correlation_matrix = np.corrcoef(predictions, rowvar=False)

    # prints the correlation matrix
    print("Correlation Matrix:\n", correlation_matrix)


    # prints the report (it works only with a single label, now we have 2)
    #print('report: ')
    #print(report)

    # alternative method to calculate accuracy
    calculateAccuracy(multi_target_forest, X_test, y_test)

    # saves trained model
    dump(multi_target_forest, 'py_cache/recipe_model.joblib')
    print("model saved: py_cache/recipe_model.joblib")
    return multi_target_forest

trainTest()