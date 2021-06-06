from data import points, labels
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)

classifier = SVC(kernel = "rbf", gamma = 0.1)
classifier.fit(training_data, training_labels)
print(classifier.score(validation_data, validation_labels))