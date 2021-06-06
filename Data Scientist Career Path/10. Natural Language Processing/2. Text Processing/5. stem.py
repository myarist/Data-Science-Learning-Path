from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

populated_island = 'Java is an Indonesian island in the Pacific Ocean. It is the most populated island in the world, with over 140 million people.'

island_tokenized = word_tokenize(populated_island)

stemmed = [stemmer.stem(token) for token in island_tokenized]

try:
  print('A stemmer exists:')
  print(stemmer)
except:
  print('Expected a variable called `stemmer`')
try:
  print('Words Tokenized:')
  print(island_tokenized)
except:
  print('Expected a variable called `island_tokenized`')
try:
  print('Stemmed Words:')
  print(stemmed)
except:
  print('Expected a variable called `stemmed`')
  