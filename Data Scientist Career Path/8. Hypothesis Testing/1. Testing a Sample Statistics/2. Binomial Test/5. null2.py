import numpy as np
import pandas as pd

null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
  
  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the minimum and maximum values in null_outcomes here:
null_min = np.min(null_outcomes) 
print(null_min)
 
null_max = np.max(null_outcomes)
print(null_max)
