# Import packages
import numpy as np
import pandas as pd

# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save author ages to author_ages
author_ages = greatest_books['Ages']

# Use numpy to calculate the median age of the top 100 authors
median_age = np.median(author_ages)

print("The median age of the 100 greatest authors, according to a survey by Le Monde is: " + str(median_age))