from cars import training_points, training_labels, testing_points, testing_labels
from sklearn.tree import DecisionTreeClassifier

print(training_points[0])
print(training_labels[0])
classifier = DecisionTreeClassifier()
classifier.fit(training_points, training_labels)
print(classifier.score(testing_points, testing_labels))