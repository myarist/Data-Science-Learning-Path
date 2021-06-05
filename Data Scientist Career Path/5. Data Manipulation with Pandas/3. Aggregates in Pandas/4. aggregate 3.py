import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

print(cheap_shoes)