import codecademylib3
import pandas as pd

nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Show the first few rows of nyc_trees
print(nyc_trees.head())

# Which columns are categorical vars?
categorical_vars = ['status',	'health',	'spc_common',	'neighborhood']

