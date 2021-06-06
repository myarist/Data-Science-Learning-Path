from spam_data import training_spam_docs, training_doc_tokens, training_labels, training_docs
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

test_text = """
Play around with the spam classifier!
"""

bow_vectorizer = CountVectorizer()

training_vectors = bow_vectorizer.fit_transform(training_docs)
test_vectors = bow_vectorizer.transform([test_text])

spam_classifier = MultinomialNB()
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.predict(test_vectors)

print("Looks like a normal email!" if predictions[0] == 0 else "You've got spam!")