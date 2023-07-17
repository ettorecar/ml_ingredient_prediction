from matplotlib.colors import LinearSegmentedColormap
from adjustText import adjust_text
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from constants import *
import numpy as np

def create_matrix_for_plot(poke_dataset):
    print('Create a Matrix for the scatter Diagram')
    # Inizializza una matrice di zeri con una riga per ogni ingrediente
    matrix = np.zeros((len(ingredient_list), len(ingredient_list)))

    # Per ogni piatto, aumenta di 1 il conteggio per ogni coppia di ingredienti nel piatto
    for poke in poke_dataset:
        for i in range(num_com):
            for j in range(i + 1, num_com):
                # Trova gli indici di questi ingredienti nella ingredient_list
                i_index = ingredient_list.index(poke[i])
                j_index = ingredient_list.index(poke[j])

                # Aumenta di 1 il conteggio per questa coppia di ingredienti
                matrix[i_index, j_index] += 1
                matrix[j_index, i_index] += 1

    return matrix

'''
def scatter_ingredienti_old(ingredient_matrix):
    print('Scatter ingredienti')
    # Riduci a 2 dimensioni con PCA.
    pca = PCA(n_components=2)
    points = pca.fit_transform(ingredient_matrix)

    # Disegna i punti.
    cmap = plt.get_cmap('rainbow')

    for i, ingredient in enumerate(ingredient_list):
        plt.scatter(
            points[i, 0],
            points[i, 1],
            color=cmap(i / len(ingredient_list)),
            label=ingredient,
            alpha=0.5
        )
        print(ingredient + ", x: {:.2f}, y: {:.2f}".format(points[i, 0], points[i, 1]))

    plt.legend(fontsize='xx-small') 
    plt.show()
'''

def scatter_ingredients(poke_dataset):
    print('Plot Scatter Diagram for Ingredients')

    ingredients_matrix = create_matrix_for_plot(poke_dataset)
    # Riduci a 2 dimensioni con PCA.
    pca = PCA(n_components=2)
    points = pca.fit_transform(ingredients_matrix)

    # Crea un istogramma 2D dei punti
    bins = 50  # Numero di bin
    H, xedges, yedges = np.histogram2d(points[:, 0], points[:, 1], bins=bins)

    # Creazione di una colormap personalizzata con bianco per densità 0
    cmap_colors = [(1.0, 1.0, 1.0)] + plt.cm.rainbow(np.linspace(0, 1, 255)).tolist()
    cmap = LinearSegmentedColormap.from_list('CustomCmap', cmap_colors, len(cmap_colors))

    # Disegna il grafico dell'istogramma con colormap personalizzata
    plt.imshow(H.T, origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap=cmap, aspect='auto')

    # Aggiungi colorbar
    cbar = plt.colorbar()
    cbar.set_label('Density')

    # Etichetta gli ingredienti
    texts = []
    for i, ingredient in enumerate(ingredient_list):
        texts.append(plt.text(points[i, 0], points[i, 1], ingredient, fontsize='xx-small', ha='center', va='center'))

    # Posiziona le etichette dei testi in modo non sovrapposto
    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))

    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.title('Scatter Ingredients')

    plt.show()

def plotFeatures(multi_target_forest, X_train, y_train):
    for i in range(y_train.shape[1]):
        RF_model = multi_target_forest.estimators_[i]
        importances = RF_model.feature_importances_
        indices = np.argsort(importances)

        plt.figure(i)
        plt.title('Importance of features for output {}'.format(i))
        plt.barh(range(X_train.shape[1]), importances[indices], color='b', align='center')
        plt.yticks(range(X_train.shape[1]), [ingredient_list[i] for i in indices])
        plt.xlabel('Relative Importance')
        plt.show()

