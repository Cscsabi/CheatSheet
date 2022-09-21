# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:08:02 2021

@author: user
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.io.common import urlopen
from sklearn.tree import DecisionTreeClassifier, plot_tree

random_state = 2021
url = 'https://arato.inf.unideb.hu/ispany.marton/MachineLearning/Datasets/banknote_authentication.txt';
raw_data = urlopen(url);
data = np.loadtxt(raw_data, delimiter=",", dtype=float)

df = pd.DataFrame(data=data, columns=None)

print(df.head(1))

print("Attributomok száma: ", df.shape[1])
print("Recordok száma: ", df.shape[0])

for each in df.columns:
    print(each, " | ", "Átlag", df[each].mean(), end=" | ")
    print("Szórás", df[each].std())

X = data[:, 0:-1]
y = data[:, -1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

crit = 'gini'
depth = 4
# Instance of decision tree class
class_tree = DecisionTreeClassifier(criterion=crit, max_depth=depth)
# Fitting decision tree on training dataset
class_tree.fit(X_train, y_train)
score_train = class_tree.score(X_train, y_train)
score_test = class_tree.score(X_test, y_test)

y_pred_gini = class_tree.predict(X_test)

fig = plt.figure(1, figsize=(40, 35), dpi=80)
plot_tree(class_tree, feature_names=df.columns,
          filled=True, fontsize=8)

plt.show()
gini_score = class_tree.score(X_test, y_test)
print(gini_score, "GINI SCORE")