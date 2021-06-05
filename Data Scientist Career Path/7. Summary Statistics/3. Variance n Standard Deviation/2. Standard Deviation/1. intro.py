import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from data import nba_data, okcupid_data

plt.hist(nba_data, alpha = 0.75, label = "NBA Data", bins = 20)
plt.hist(okcupid_data, alpha = 0.5, label = "OkCupid Data", bins = 20)
plt.xlabel("Height (inches)")
plt.legend()
plt.show()

print("The variance of the NBA dataset is " +str(np.var(nba_data)))
print("The variance of the OkCupid dataset is " +str(np.var(okcupid_data)) + "\n")
print("The mean of the NBA dataset is " +str(np.mean(nba_data)) + " inches")
print("The mean of the OkCupid dataset is " +str(np.mean(okcupid_data)) + " inches")