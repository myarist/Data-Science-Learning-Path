import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

#calculate the number of simulated visitors who made a purchase:
num_purchased = np.sum(simulated_monthly_visitors == 'y')
print(num_purchased)

print(num_purchased)