import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
movies = pd.read_csv("movie_show.csv", index_col=0)

# Print the first five rows of the dataframe
print(movies.head())

# Print the data types of the dataframe
print(movies.dtypes)

# Replace any missing values in release_year with 2019
movies['release_year'] = movies['release_year'].replace(['missing'], 2019)

# Change the data type of release_year to int
movies['release_year'] = pd.to_numeric(movies['release_year'])

# Recheck the data types with .dtypes.
print(movies.dtypes)

# Calculate the mean of release_year
print(movies['release_year'].mean())