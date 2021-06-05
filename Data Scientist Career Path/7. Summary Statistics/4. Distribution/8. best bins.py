# Import packages
import codecademylib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use plt.hist() below
plt.hist(times, range=(0, 24), bins=24,  edgecolor="black")
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")

plt.show()