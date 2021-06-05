import codecademylib
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID','Title','Category','Year Released','Rating']
print(df)