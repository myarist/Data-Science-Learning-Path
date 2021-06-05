from scipy.stats import f_oneway
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run ANOVA
fstat, pval = f_oneway(a, b, c)
print(pval)

# determine significance
significant = True