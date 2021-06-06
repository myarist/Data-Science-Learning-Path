from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 

survey_text = 'A YouGov study found that American\'s like Italian food more than any other country\'s cuisine.'

stop_words = set(stopwords.words('english')) 

tokenized_survey = word_tokenize(survey_text) 

text_no_stops = [word for word in tokenized_survey if word not in stop_words]

try:
  print(f'Stopwords type: {type(stop_words)}')
except:
  print('Expected a variable called `stop_words`')
try:
  print(f'Words Tokenized: {tokenized_survey}')
except:
  print('Expected a variable called `tokenized_survey`')
try:
  print(f'Text without Stops: {text_no_stops}')
except:
  print('Expected a variable called `text_no_stops`')
  