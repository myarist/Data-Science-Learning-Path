import codecademylib3_seaborn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook, x="name", y="grade", ci="sd")
plt.show()