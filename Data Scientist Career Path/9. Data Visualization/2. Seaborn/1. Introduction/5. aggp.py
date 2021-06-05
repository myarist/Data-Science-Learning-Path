import codecademylib3_seaborn
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook, x="assignment_name", y="grade")

plt.show()
