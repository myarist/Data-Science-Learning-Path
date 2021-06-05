import codecademylib3_seaborn
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


df = pd.read_csv('survey.csv')

print(df.head())