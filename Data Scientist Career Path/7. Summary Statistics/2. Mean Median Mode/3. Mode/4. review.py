# Import packages
import codecademylib
import numpy as np
import pandas as pd
from scipy import stats

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Calculate the average and median value of the author_ages array
average_age = np.average(author_ages)
median_age = np.median(author_ages)
mode_age = 38

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Author Ages at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=3, label="Mean")
plt.axvline(median_age, color='y', linestyle='dotted', linewidth=3, label="Median")
plt.axvline(mode_age, color='orange', linestyle='dashed', linewidth=3, label="Mode")
plt.legend()

plt.show()