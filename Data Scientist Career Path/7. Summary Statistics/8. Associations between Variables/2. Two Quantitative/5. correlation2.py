import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

sleep = pd.read_csv('sleep_performance.csv')

# create your scatter plot here:
plt.scatter(sleep.hours_sleep, sleep.performance)
plt.xlabel('Hours of Sleep')
plt.ylabel('Performance')
plt.show()

# calculate the correlation for `hours_sleep` and `performance`:
corr_sleep_performance, p = pearsonr(sleep.hours_sleep, sleep.performance)
print(corr_sleep_performance)
