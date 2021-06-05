import numpy as np
from data import nba_data, okcupid_data

nba_variance = np.var(nba_data)
okcupid_variance = np.var(okcupid_data)

#Change these variables to be the standard deviation of each dataset.
nba_standard_deviation = nba_variance ** (1/2)
okcupid_standard_deviation = okcupid_variance ** (1/2)

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))