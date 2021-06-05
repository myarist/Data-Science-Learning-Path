import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
import seaborn as sns

students = pd.read_csv('students.csv')

#create the boxplot here:
sns.boxplot(data = students, x = 'address', y = 'G3')
plt.show()