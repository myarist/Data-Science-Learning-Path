import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.xlabel('Number of beds')
plt.ylabel('Number of sqfeet')
plt.show()

plt.show()