# Import packages
import numpy as np
import pandas as pd

# Read author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Set author ages to a NumPy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))