from sklearn.feature_extraction.text import CountVectorizer

sentence = "It was the best of times, it was the worst of times."
print(sentence)

# preprocessing
sentence_lst = [word.lower().strip(".") for word in sentence.split()]

# set context_length
context_length = 3

# function to get cbows
def get_cbows(sentence_lst, context_length):
  cbows = list()
  for i, val in enumerate(sentence_lst):
    if i < context_length:
      pass
    elif i < len(sentence_lst) - context_length:
      context = sentence_lst[i-context_length:i] + sentence_lst[i+1:i+context_length+1]
      vectorizer = CountVectorizer()
      vectorizer.fit_transform(context)
      context_no_order = vectorizer.get_feature_names()
      cbows.append((val,context_no_order))
  return cbows

# define cbows here:
cbows = get_cbows(sentence_lst, context_length)

# function to get cbows
def get_skip_grams(sentence_lst, context_length):
  skip_grams = list()
  for i, val in enumerate(sentence_lst):
    if i < context_length:
      pass
    elif i < len(sentence_lst) - context_length:
      context = sentence_lst[i-context_length:i] + sentence_lst[i+1:i+context_length+1]
      skip_grams.append((val, context))
  return skip_grams

# define skip_grams here:
skip_grams = get_skip_grams(sentence_lst, context_length)

try:
  print('\nContinuous Bag of Words')
  for cbow in cbows:
    print(cbow)
except:
  pass
try:
  print('\nSkip Grams')
  for skip_gram in skip_grams:
    print(skip_gram)
except:
  pass