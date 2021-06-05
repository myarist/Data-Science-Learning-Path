import codecademylib
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name'],axis=1)