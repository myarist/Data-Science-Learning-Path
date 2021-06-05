# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = np.mean(author_ages)
median_age = np.median(author_ages)

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="mean")
plt.axvline(median_age, color='y', linestyle='dotted', linewidth=3, label="median")
plt.legend()

plt.show()