from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

ecg_text = 'An electrocardiogram is used to record the electrical conduction through a person\'s heart. The readings can be used to diagnose cardiac arrhythmias.'

tokenized_by_word = word_tokenize(ecg_text)
tokenized_by_sentence = sent_tokenize(ecg_text)

try:
  print('Word Tokenization:')
  print(tokenized_by_word)
except:
  print('Expected a variable called `tokenized_by_word`')
try:
  print('Sentence Tokenization:')
  print(tokenized_by_sentence)
except:
  print('Expected a variable called `tokenized_by_sentence`')