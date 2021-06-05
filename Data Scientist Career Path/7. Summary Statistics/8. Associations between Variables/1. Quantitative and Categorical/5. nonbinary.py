import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3

students = pd.read_csv('students.csv')

#create the box-plot here:
sns.boxplot(data=students, x='Fjob', y='G3')
plt.show()


