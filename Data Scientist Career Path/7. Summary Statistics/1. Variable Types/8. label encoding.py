import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
clothes = pd.read_csv('clothing.csv', index_col=0)

# Check the first five rows of the `clothes` dataframe with `.head()`.
print(clothes.head())

# Change the data type of `Rating` to category
clothes['Rating'] = pd.Categorical(clothes['Rating'], ['very unsatisfied', 'unsatisfied', 'neutral', 'satisfied', 'very satisfied'], ordered=True)

# Check the order of the Rating column
print(clothes['Rating'].unique())

# Create rating_codes by encoding the `Rating` variable with .cat.codes 
clothes['rating_codes'] = clothes['Rating'].cat.codes

# Print the first five rows of the dataframe
print(clothes.head())