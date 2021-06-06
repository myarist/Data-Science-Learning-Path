import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from poems import poems
from preprocessing import preprocess_text

# preprocess documents
processed_poems = [preprocess_text(poem) for poem in poems]

# initialize and fit TfidfVectorizer
vectorizer = TfidfVectorizer(norm=None)
tfidf_scores = vectorizer.fit_transform(processed_poems)

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()

# get corpus index
corpus_index = [f"Poem {i+1}" for i in range(len(poems))]

# create pandas DataFrame with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=corpus_index)
  print(df_tf_idf)
except:
  pass