import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41, color = 'r')
plt.show()