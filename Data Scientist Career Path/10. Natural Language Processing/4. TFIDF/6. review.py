import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from raven import the_raven_stanzas
from preprocessing import preprocess_text

# view first stanza
print(the_raven_stanzas[0])

# preprocess documents
processed_stanzas = [preprocess_text(stanza) for stanza in the_raven_stanzas]

# initialize and fit TfidfVectorizer
vectorizer = TfidfVectorizer(norm=None)
tfidf_scores = vectorizer.fit_transform(processed_stanzas)

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()

# get stanza index
stanza_index = [f"Stanza {i+1}" for i in range(len(the_raven_stanzas))]

# create pandas DataFrame with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=stanza_index)
  print(df_tf_idf)
except:
  pass