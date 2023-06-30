from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
import numpy as np
#X, y1 = make_classification(n_samples=10, n_features=100, n_informative=30, n_classes=3, random_state=1)

X, y1 = make_classification(n_samples=100, n_features=10, n_informative=10, n_classes=1, random_state=1)

y2 = shuffle(y1, random_state=1)
y3 = shuffle(y1, random_state=2)
Y = np.vstack((y1, y2, y3)).T
n_samples, n_features = X.shape  # 10,100
n_outputs = Y.shape[1]  # 3
n_classes = 3
forest = RandomForestClassifier(random_state=1)
multi_target_forest = MultiOutputClassifier(forest, n_jobs=2)
predictions = multi_target_forest.fit(X, Y).predict(X)
#predictions = multi_target_forest.predict(X) #non so che differenza c'è se la scrivo così
print(predictions)
