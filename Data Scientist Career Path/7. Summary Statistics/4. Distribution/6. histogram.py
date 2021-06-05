# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use numpy.histogram() below
times_hist = np.histogram(times, range=(0,24), bins=4)

print(times_hist)