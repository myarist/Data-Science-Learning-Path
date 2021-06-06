import codecademylib3_seaborn
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy
from sklearn.cluster import KMeans

std = 0.5

x = np.append(np.append(np.append(np.random.normal(0.25,std,100), np.random.normal(0.75,std,100)), np.random.normal(0.25,std,100)), np.random.normal(0.75,std,100))

y = np.append(np.append(np.append(np.random.normal(0.25,std,100), np.random.normal(0.25,std,100)), np.random.normal(0.75,std,100)), np.random.normal(0.75,std,100))

values = np.array(list(zip(x, y)))

centroids_x = [2.5, 2.5]
centroids_y = [1, 3]

centroids = np.array(list(zip(centroids_x, centroids_y)))

model_custom = KMeans(init=centroids, n_clusters=2)
results_custom = model_custom.fit_predict(values)

model = KMeans(init='k-means++', n_clusters=2)
results = model.fit_predict(values)

plt.scatter(x, y, c=results_custom, alpha=1)
plt.scatter(model_custom.cluster_centers_[:, 0], model_custom.cluster_centers_[:, 1], marker='v', s=100)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='D', s=100)
plt.title('Custom Initialization')
plt.show()
plt.cla()

plt.scatter(x, y, c=results, alpha=1)
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], marker='v', s=100)
plt.title('K-Means++ Initialization')
plt.show()

print("The custom model's inertia is " + str(model_custom.inertia_))
print("The K-means++ model's inertia is " + str(model.inertia_))
