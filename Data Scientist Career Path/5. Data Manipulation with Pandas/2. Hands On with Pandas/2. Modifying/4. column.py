import codecademylib
from string import lower
import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df['Lowercase Name'] = df['Name'].apply(lower)
print(df)