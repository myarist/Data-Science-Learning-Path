import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
cereal = pd.read_csv('cereal.csv', index_col=0)

# Show the first five rows of the `cereal` dataframe
print(cereal.head())

# Create a new dataframe with the `mfr` variable One-Hot Encoded
cereal = pd.get_dummies(cereal, columns=['mfr'])

# Show first five rows of new dataframe
print(cereal.head())
