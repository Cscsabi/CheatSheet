# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:02:08 2021

@author: kapla
"""

import numpy as np
import pandas as pd
from urllib.request import urlopen;  # importing url handling

import matplotlib.colors as col
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from pandas.plotting import andrews_curves
from pandas.plotting import scatter_matrix
from pandas.plotting import parallel_coordinates
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import davies_bouldin_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree    
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, roc_curve, auc, plot_roc_curve

#1.feladat

url = "https://arato.inf.unideb.hu/ispany.marton/MachineLearning/Datasets/letter-recognition.csv"
df = pd.read_csv(url, sep =",")

classes= df.columns.values.tolist()
data = df.values


print(classes)
print(data)

x = data [:,1:17] #•adatok
y = data[:,0] #osztalyok

print("Osztalyok szama:",len(y))




#2.feladat

group = df.groupby(by='lettr')

print(group.mean())
print(group.std())


#3.feladat

scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal="kde");
parallel_coordinates(df, "lettr");


#4.feladat
#nemjo de legalabb van az 5oshoz adat 

#filtered = df[df['lettr'].str.contains('I|O')]
#print(filtered)

#x1 = filtered [:,1:17] #•adatok
#y1 = filtered[:,0] #osztalyok

#print(x1)
#print(y1)

X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.3);
#5.feladat
#print(X_train)


crit = 'gini'
depth =4

class_tree = DecisionTreeClassifier(criterion=crit,max_depth=depth)

class_tree.fit(X_train, y_train)
score_train = class_tree.score(X_train, y_train)
score_test_tree = class_tree.score(X_test, y_test)
y_pred_gini = class_tree.predict(X_test)
print(score_test_tree)

#Logisztikus regresszió
logreg_classifier = LogisticRegression(solver='liblinear')
logreg_classifier.fit(X_train,y_train)
ypred_logreg = logreg_classifier.predict(X_train)
score_logreg_train = logreg_classifier.score(X_train,y_train)
cm_logreg_train = confusion_matrix(y_train, ypred_logreg)
ypred_logreg = logreg_classifier.predict(X_test)
cm_logreg_test = confusion_matrix(y_test, ypred_logreg)
yprobab_logreg = logreg_classifier.predict_proba(X_test)
score_test_logreg = logreg_classifier.score(X_test,y_test)
print(score_test_logreg)

#Neurális háló
neural_classifier = MLPClassifier(hidden_layer_sizes=(3),activation='logistic',max_iter=1000)
neural_classifier.fit(X_train,y_train)
ypred_neural = neural_classifier.predict(X_train) 
score_train_neural = neural_classifier.score(X_train,y_train)
cm_neural_train = confusion_matrix(y_train, ypred_neural)
ypred_neural = neural_classifier.predict(X_test)
cm_neural_test = confusion_matrix(y_test, ypred_neural)
score_test_neural = neural_classifier.score(X_test,y_test) 
yprobab_neural = neural_classifier.predict_proba(X_test) 
print(score_test_neural)



print(f'Test score of tree in %: {score_test_tree*100}')
print(f'Test score of logreg in %: {score_test_logreg*100}')
print(f'Test score of neural in %: {score_test_neural*100}')




#6.feladat
"""
from sklearn.tree import DecisionTreeClassifier, plot_tree
classifier = DecisionTreeClassifier(criterion=crit,max_depth=depth)

classifier.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix, plot_confusion_matrix, roc_curve, auc, plot_roc_curve; 
plot_confusion_matrix(classifier, X_test, y_test);
plot_roc_curve(classifier, X_test, y_test);

"""


plot_roc_curve(neural_classifier, X_test, y_test);

fpr_neural, tpr_neural, _ = roc_curve(y_test, yprobab_neural[:,1]);
roc_auc_neural = auc(fpr_neural, tpr_neural);
print(roc_auc_neural)


#7.feladat

import numpy as np;  # Numerical Python library
import matplotlib.pyplot as plt;  # Matlab-like Python module
from sklearn.datasets import load_iris;  # importing data loader
from sklearn.cluster import KMeans; # Class for K-means clustering
from sklearn.metrics import davies_bouldin_score;  # function for Davies-Bouldin goodness-of-fit 
from sklearn.decomposition import PCA; #  Class for Principal Component analysis
# 10 26 30

kmeans = KMeans(n_clusters=10, random_state=2021);
kmeans.fit(x);
labels = kmeans.labels_;
centers = kmeans.cluster_centers_;
DB10 = davies_bouldin_score(x,labels);  
print("10nel az index:",DB10)

kmeans = KMeans(n_clusters=26, random_state=2021);
kmeans.fit(x);
labels = kmeans.labels_;
centers = kmeans.cluster_centers_;
DB26 = davies_bouldin_score(x,labels);  
print("26nal az index:",DB26)

kmeans = KMeans(n_clusters=30, random_state=2021);
kmeans.fit(x);
labels = kmeans.labels_;
centers = kmeans.cluster_centers_;
DB30 = davies_bouldin_score(x,labels);  
print("30nal az index:",DB30)

kmeans = KMeans(n_clusters=26, random_state=2021);
kmeans.fit(x);
labels = kmeans.labels_;
centers = kmeans.cluster_centers_;
score = kmeans.score(x);

pca = PCA(n_components=2);
pca.fit(x);
data_pc = pca.transform(x);
centers_pc = pca.transform(centers);

fig = plt.figure(1);
plt.title('Clustering of the Iris data after PCA');
plt.xlabel('PC1');
plt.ylabel('PC2');
plt.scatter(data_pc[:,0],data_pc[:,1],s=50,c=labels);
plt.scatter(centers_pc[:,0],centers_pc[:,1],s=200,c='red',marker='X');
plt.legend();
plt.show();


