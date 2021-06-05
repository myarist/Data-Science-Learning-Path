import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("movie_show.csv")

# View the first five rows of the dataframe
print(movies.head())

release_year_variable_type = 'discrete'
print(release_year_variable_type)

duration_variable_type = 'continuous'
print(duration_variable_type)