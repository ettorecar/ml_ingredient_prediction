from matplotlib.colors import LinearSegmentedColormap
from adjustText import adjust_text
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from constants import *
import numpy as np

def create_matrix_for_plot(recipe_dataset):
    print('Create a Matrix for the scatter Diagram')
    # initializes a zeros matrix with a row for each ingredients
    matrix = np.zeros((len(ingredient_list), len(ingredient_list)))

    # for each recipe, increase by 1 the count for each couple of ingredients
    for recipe in recipe_dataset:
        for i in range(num_com):
            for j in range(i + 1, num_com):
                # finds indexes of these ingredients in ingredient_list
                i_index = ingredient_list.index(recipe[i])
                j_index = ingredient_list.index(recipe[j])

                # increase by 1 the count for this couple of ingredients
                matrix[i_index, j_index] += 1
                matrix[j_index, i_index] += 1

    return matrix

'''
def scatter_ingredients_old(ingredient_matrix):
    print('Scatter ingredients')
    #  reduces to 2 sizes with PCA.
    pca = PCA(n_components=2)
    points = pca.fit_transform(ingredient_matrix)

    # draws the points.
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

def scatter_ingredients(recipe_dataset):
    '''
    this method draws a scatterplot of the ingredients, starting from the dataset.
    It is not correlated to the model, since it is a preliminar analysis, based only on input data.
    '''
    print('Plot Scatter Diagram for Ingredients')

    ingredients_matrix = create_matrix_for_plot(recipe_dataset)
    # reduces to 2 sizes with PCA.
    pca = PCA(n_components=2)
    points = pca.fit_transform(ingredients_matrix)

    # creates 2D histogram of points
    bins = 50  # Num of bin
    H, xedges, yedges = np.histogram2d(points[:, 0], points[:, 1], bins=bins)

    # creates a customized colormap with white for 0 density 
    cmap_colors = [(1.0, 1.0, 1.0)] + plt.cm.rainbow(np.linspace(0, 1, 255)).tolist()
    cmap = LinearSegmentedColormap.from_list('CustomCmap', cmap_colors, len(cmap_colors))

    # draws histogram graphic with customized colormap
    plt.imshow(H.T, origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap=cmap, aspect='auto')

    # adds colorbar
    cbar = plt.colorbar()
    cbar.set_label('Density')

    # labels ingredients
    texts = []
    for i, ingredient in enumerate(ingredient_list):
        texts.append(plt.text(points[i, 0], points[i, 1], ingredient, fontsize='xx-small', ha='center', va='center'))

    # places text labels in a non-overlapping way
    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))

    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.title('Scatter Ingredients')

    plt.show()

def plotFeatures(multi_target_forest, X_train, y_train):
    '''
    this method plot a diagram that shows the importance of the features
    currently it seems not accurate, we have to review the code.
    '''
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