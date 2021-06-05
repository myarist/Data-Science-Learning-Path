import pandas as pd
from scipy.stats import chi2_contingency

data = pd.read_csv("ab_data.csv")
print(data.head())

# calculate contingency table here
ab_contingency = pd.crosstab(data.Web_Version, data.Purchased)
print(ab_contingency)

# run your chi square test here
chi2, pval, dof, expected = chi2_contingency(ab_contingency)
print(pval)