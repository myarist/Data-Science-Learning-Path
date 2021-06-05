import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max()

pricey_shoes = pricey_shoes.reset_index()

print(pricey_shoes)
print(type(pricey_shoes))