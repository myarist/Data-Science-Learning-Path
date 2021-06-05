import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("movie_show.csv", index_col=0)

# View the first five rows of the dataframe
print(movies.head())

# Print the data types of the dataframe with dtypes
print(movies.dtypes)