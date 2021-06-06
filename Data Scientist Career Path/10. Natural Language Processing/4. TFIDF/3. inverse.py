import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from term_frequency import term_frequencies, feature_names, df_term_frequencies

# display term-document matrix of term frequencies
print(df_term_frequencies)

# initialize and fit TfidfTransformer
transformer = TfidfTransformer()
transformer.fit(term_frequencies)
idf_values = transformer.idf_

# create pandas DataFrame with inverse document frequencies
try:
  df_idf = pd.DataFrame(idf_values, index = feature_names, columns=['Inverse Document Frequency'])
  print(df_idf)
except:
  pass