import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

print(orders.head(10))

most_expensive = orders.price.max()

num_colors = orders.shoe_color.nunique()