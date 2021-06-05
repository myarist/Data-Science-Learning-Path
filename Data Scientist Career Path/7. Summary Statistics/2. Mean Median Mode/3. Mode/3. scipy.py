# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save author ages to author_ages
author_ages = greatest_books['Ages']

# Use numpy to calculate the mode age of the top 100 authors
mode_age = stats.mode(author_ages)

print("The mode age and its frequency of authors from Le Monde's 100 greatest books is: " + str(mode_age[0][0]) + " and " + str(mode_age[1][0]))