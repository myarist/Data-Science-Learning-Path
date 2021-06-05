import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#create the overlapping histograms here:
plt.hist(scores_urban, color="blue", label="Urban", normed=True, alpha=0.5)
plt.hist(scores_rural, color="red", label="Rural", normed=True, alpha=0.5)
plt.legend()
plt.show()