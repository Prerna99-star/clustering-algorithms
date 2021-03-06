# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:28:29 2020

Hierarchical clustering
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values 

# Using dendogram for finding optimal no. of clusrters

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

#fitting hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

#visualising the clusters

plt.scatter(
    X[y_hc == 0, 0], X[y_hc == 0, 1],
    s =100, c='red',label= 'Cluster 1'
    )
plt.scatter(
    X[y_hc ==1, 0], X[y_hc ==1, 1],
    s =100, c='blue', label= 'Cluster 2'
    )
plt.scatter(
    X[y_hc ==2, 0], X[y_hc ==2, 1],
    s =100, c='green',label= 'Cluster 3'
    )
plt.scatter(
    X[y_hc ==3, 0], X[y_hc ==3, 1],
    s =100, c='cyan',  label= 'Cluster 4'
    )
plt.scatter(
    X[y_hc ==4, 0], X[y_hcs ==4, 1], 
    s =100, c='magenta', label= 'Cluster 5'
    )

plt.title('Cluster of Clients')
plt.xlabel('Annual Income')
plt.ylabel('Spending score')
plt.legend(scatterpoints=1)
plt.show()