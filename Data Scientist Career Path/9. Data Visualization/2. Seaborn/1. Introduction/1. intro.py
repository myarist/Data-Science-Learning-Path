import codecademylib3_seaborn
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt

# Paste import here:
import seaborn as sns

df = pd.read_csv('survey.csv')
sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
plt.show()