import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print(orders)
print(products)

merged_df = orders.merge(products)

print(merged_df)