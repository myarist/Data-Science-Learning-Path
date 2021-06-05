import pandas as pd

# Get NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census.csv")

health_proportions = nyc_trees['health'].value_counts(normalize=True)

health_proportions_2 = nyc_trees['health'].value_counts(dropna=False, normalize=True)