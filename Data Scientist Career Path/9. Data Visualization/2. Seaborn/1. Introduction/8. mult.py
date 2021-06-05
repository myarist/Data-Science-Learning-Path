import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")

sns.barplot(data=df,
            x="Age Range",
            y="Response",
            hue="Gender")

plt.show()