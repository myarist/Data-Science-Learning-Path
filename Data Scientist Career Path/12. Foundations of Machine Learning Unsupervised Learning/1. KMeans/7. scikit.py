import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

# Create a model that finds 3 clusters
model = KMeans(n_clusters=3)

# Fit the model to samples
model.fit(samples)

# Determine the labels of samples 
labels = model.predict(samples)

# Print the labels
print(labels)
