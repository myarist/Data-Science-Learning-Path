import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(
    orders,
    products,
    left_on='product_id',
    right_on='id',
    suffixes=['_orders', '_products']
)

print(orders_products)