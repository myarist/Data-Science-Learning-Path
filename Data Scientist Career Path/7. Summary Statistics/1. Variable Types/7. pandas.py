import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
clothes = pd.read_csv('clothing.csv', index_col=0)

# View the first five rows of the dataframe
print(clothes.head())

# Print the unique values of the `Rating` column
print(clothes['Rating'].unique())

# Change the data type of `Rating` to category
clothes['Rating'] = pd.Categorical(clothes['Rating'], ['very unsatisfied', 'unsatisfied', 'neutral', 'satisfied', 'very satisfied'], ordered=True)

# Recheck the values of `Rating` with .unique()
print(clothes['Rating'].unique())