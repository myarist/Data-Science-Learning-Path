from scipy.stats import ttest_ind
import codecademylib3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run t-tests
_, a_b_pval = ttest_ind(a,b)
_, a_c_pval = ttest_ind(a,c)
_, b_c_pval = ttest_ind(b,c)
print(a_b_pval)
print(a_c_pval)
print(b_c_pval)

# determine significance
a_b_significant = True
a_c_significant = True
b_c_significant = False

# create plot
sns.boxplot(data=veryants, x='Store', y='Sale')
plt.show()