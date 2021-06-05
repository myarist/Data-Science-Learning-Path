import numpy as np
from data import nba_data, okcupid_data

#Change these variables to be the standard deviation of each dataset. Use NumPy's function!
nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))