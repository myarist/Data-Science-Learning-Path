import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# pre-set values
significance_threshold = 0.05
sample_size = 100
lift = .3
control_rate = .5
name_rate = (1 + lift) * control_rate

# simulate a dataset
sample_control = np.random.choice(['yes', 'no'], size=int(sample_size/2), p=[control_rate,1-control_rate])
sample_name = np.random.choice(['yes', 'no'], size=int(sample_size/2), p=[name_rate, 1-name_rate])

group = ['control']*int(sample_size/2) + ['name']*int(sample_size/2)
outcome = list(sample_control) + list(sample_name)
sim_data = {"Email": group, "Opened": outcome}
sim_data = pd.DataFrame(sim_data)

# run a chi-square test
ab_contingency = pd.crosstab(np.array(sim_data.Email), np.array(sim_data.Opened))
chi2, pval, dof, expected = chi2_contingency(ab_contingency, correction=False)
print("P Value:")
print(pval)

# determine significance here:
result = 'not significant'

print("Result:")
print(result)
