import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3
from scipy.stats import pearsonr
np.set_printoptions(suppress=True, precision = 1) 

penguins = pd.read_csv('penguins.csv')

#print the first few rows
print(penguins.head())

#create a scatter plot
plt.scatter(penguins.flipper_length_mm, penguins.body_mass_g)
plt.show()

#calculate covariance:
covariance_mat = np.cov(penguins.flipper_length_mm, penguins.body_mass_g)
print("covariance matrix: ")
print(covariance_mat)

print("covariance: ", covariance_mat[1][0])

#calculate correlation:
correlation, p = pearsonr(penguins.flipper_length_mm, penguins.body_mass_g)
print("correlation: ", correlation)