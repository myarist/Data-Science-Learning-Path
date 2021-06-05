# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
mu, sigma = 800, 100 # mean and standard deviation
burrito_calories = np.random.normal(mu, sigma, 320)

# Save transaction times to a separate numpy array
plt.hist(burrito_calories, range=(250, 1250), bins=100,  edgecolor='black')
plt.title("Calories in a Burrito Bowl", fontsize = 24)
plt.xlabel("Calories", fontsize=18)
plt.ylabel("Count", fontsize=18)

plt.show()