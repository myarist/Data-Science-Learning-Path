import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3

titanic = pd.read_csv('titanic.csv')

print(titanic.head())

#separate out fares by survival
fares_died = titanic.Fare[titanic.Survived == 0]
fares_survived = titanic.Fare[titanic.Survived == 1]

#mean difference
mean_fare_died = np.mean(fares_died)
mean_fare_surv = np.mean(fares_survived)
mean_diff = mean_fare_surv-mean_fare_died
print('mean difference: ')
print(mean_diff)

#median difference
med_fare_died = np.median(fares_died)
med_fare_surv = np.median(fares_survived)
med_diff = med_fare_surv-med_fare_died
print("median difference: ")
print(med_diff)

#create subplots (scroll to see plots)
fig = plt.figure(figsize = (10,20))

#create the boxplot:
ax = fig.add_subplot(2,1,1)
ax = sns.boxplot(data = titanic, x = 'Survived', y = 'Fare')

#create the histograms:
ax = fig.add_subplot(2,1,2)
ax = plt.hist(fares_died, color="blue", label="Died", normed=True, alpha=0.5)
ax = plt.hist(fares_survived, color="red", label="Survived", normed=True, alpha=0.5)
ax = plt.legend()
plt.show()