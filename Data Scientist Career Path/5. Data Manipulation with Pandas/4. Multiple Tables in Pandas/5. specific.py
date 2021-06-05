import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))

print(orders_products)