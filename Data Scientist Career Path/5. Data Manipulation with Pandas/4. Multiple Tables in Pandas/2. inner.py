import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)
print(products)
print(customers)

order_3_description = 'thing-a-ma-jig'
order_5_phone_number = '112-358-1321'