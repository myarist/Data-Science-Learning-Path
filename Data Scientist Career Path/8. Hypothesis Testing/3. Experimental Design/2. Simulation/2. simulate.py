import numpy as np
import pandas as pd

sample_size = 5
lift = .3
control_rate = .5
name_rate = (1 + lift) * control_rate

sample_control = np.random.choice(['yes', 'no'], size=int(sample_size/2), p=[control_rate,1-control_rate])
sample_name = np.random.choice(['yes', 'no'], size=int(sample_size/2), p=[name_rate, 1-name_rate])

group = ['control']*int(sample_size/2) + ['name']*int(sample_size/2)
outcome = list(sample_control) + list(sample_name)
sim_data = {"Button": group, "Opened": outcome}
sim_data = pd.DataFrame(sim_data)
print(sim_data)