import pandas as pd

# Read NYC Trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

tree_status_proportions = nyc_trees['status'].value_counts(normalize=True)