import pandas as pd
import numpy as np

# Read NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census2.csv")

size_labels_ordered = ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)']

nyc_trees.tree_diam_category = pd.Categorical(nyc_trees.tree_diam_category, size_labels_ordered, ordered=True)

# Calculate 25th Percentile Category
p25_ind = np.percentile(nyc_trees['tree_diam_category'].cat.codes, 25)
p25_tree_diam_category = size_labels_ordered[int(p25_ind)]
print(p25_tree_diam_category)

# Calculate 75th Percentile Category
p75_ind = np.percentile(nyc_trees['tree_diam_category'].cat.codes, 75)
p75_tree_diam_category = size_labels_ordered[int(p75_ind)]
print(p75_tree_diam_category)