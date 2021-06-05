import pandas as pd
import numpy as np

# Read NYC trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Get unique values from `health`
tree_health_statuses = nyc_trees.health.unique()
print(tree_health_statuses)

# Ordered list of categories
health_categories = ['Poor', 'Fair', 'Good']

# Convert to categorical type
nyc_trees['health'] = pd.Categorical(
        nyc_trees['health'], health_categories, ordered=True
)

# Calculate median values
median_index = np.median(nyc_trees['health'].cat.codes)
median_health_status = health_categories[int(median_index)]
print(median_health_status)