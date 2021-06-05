import codecademylib
import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda str: str.split()[-1]
print(df)

df['last_name'] = df.name.apply(get_last_name)