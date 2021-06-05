import codecademylib3
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("games.csv")
print(df.head())

sns.countplot(df["victory_status"])
plt.show()