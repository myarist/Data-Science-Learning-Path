import numpy as np
import pandas as pd
import codecademylib3

monthly_report = pd.read_csv('monthly_report.csv')



#print the head of monthly_report:
print(monthly_report.head())

#calculate and print sample_size:
sample_size = len(monthly_report)
print(sample_size)

#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == 'y')
print(num_purchased)