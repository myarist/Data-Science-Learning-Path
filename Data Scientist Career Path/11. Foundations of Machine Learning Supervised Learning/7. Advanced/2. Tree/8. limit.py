from cars import training_points, training_labels, testing_points, testing_labels
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(random_state = 0, max_depth = 11)
classifier.fit(training_points, training_labels)
print(classifier.score(testing_points, testing_labels))
print(classifier.tree_.max_depth)