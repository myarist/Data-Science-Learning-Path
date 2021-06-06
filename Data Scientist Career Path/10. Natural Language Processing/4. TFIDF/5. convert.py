import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from term_frequency import bow_matrix, feature_names, df_bag_of_words, corpus_index

# display term-document matrix of term frequencies (bag-of-words)
print(df_bag_of_words)

# initialize and fit TfidfTransformer, transform bag-of-words matrix
transformer = TfidfTransformer(norm=None)
tfidf_scores = transformer.fit_transform(bow_matrix)

# create pandas DataFrame with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index = feature_names, columns=corpus_index)
  print(df_tf_idf)
except:
  pass