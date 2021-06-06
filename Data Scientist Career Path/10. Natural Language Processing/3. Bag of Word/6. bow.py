from preprocessing import preprocess_text
from nltk.util import ngrams
from collections import Counter

text = "It's exciting to watch flying fish after a hard day's work. I don't know why some fish prefer flying and other fish would rather swim. It seems like the fish just woke up one day and decided, 'hey, today is the day to fly away.'"
tokens = preprocess_text(text)

# Bigram approach:
bigrams_prepped = ngrams(tokens, 2)
bigrams = Counter(bigrams_prepped)
print("Three most frequent word sequences and the number of occurrences according to Bigrams:")
print(bigrams.most_common(3))

bag_of_words = Counter(tokens)
print("\nThree most frequent words and number of occurrences according to Bag of Words:")
most_common_three = bag_of_words.most_common(3)
print(most_common_three)