import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3
from scipy.stats import ttest_ind
data = pd.read_csv('version_time.csv')

#separate out times for  two versions
old = data.time_minutes[data.version=='old']
new = data.time_minutes[data.version=='new']

#run the t-test here:
tstat, pval = ttest_ind(old, new)
print(pval)

#determine significance
significant = True

#plot overlapping histograms
plt.hist(old, alpha=.8, label='old')
plt.hist(new, alpha=.8, label='new')
plt.legend()
plt.show()