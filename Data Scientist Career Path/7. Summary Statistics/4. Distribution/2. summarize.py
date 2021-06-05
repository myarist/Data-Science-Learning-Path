# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")
transactions = transactions.drop(["Unnamed: 0"], axis = 1)

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Print transactions below
print(transactions)

# Print the average times below
print(np.average(times))