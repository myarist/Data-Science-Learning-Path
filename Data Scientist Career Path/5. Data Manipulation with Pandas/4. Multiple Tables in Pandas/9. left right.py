import codecademylib
import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_left = store_a.merge(store_b, how='left')

store_b_a_left = store_b.merge(store_a, how='left')

print(store_a_b_left)
print(store_b_a_left)