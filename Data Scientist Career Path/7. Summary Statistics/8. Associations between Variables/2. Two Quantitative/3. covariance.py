import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision = 1) 

housing = pd.read_csv('housing_sample.csv')

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.sqfeet, housing.beds)
print(cov_mat_sqfeet_beds)

# store the covariance as cov_sqfeet_beds
cov_sqfeet_beds = cov_mat_sqfeet_beds[0][1]