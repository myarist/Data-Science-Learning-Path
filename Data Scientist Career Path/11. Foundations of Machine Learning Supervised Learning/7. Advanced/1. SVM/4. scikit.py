from sklearn.svm import SVC
from graph import points, labels

classifier = SVC(kernel = 'linear')
classifier.fit(points, labels)
print(classifier.predict([[3, 4], [6, 7]]))
