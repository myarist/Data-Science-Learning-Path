import codecademylib3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# add in your answers here!
left_plot = "Bar Chart"
right_plot = "Histogram"

heroes_data = pd.read_csv("heroes_information.csv")
# line of code used to clean up messy data
heroes_data_cleaned = heroes_data[heroes_data.Alignment != "-"]

#### code for left plot
plt.subplot(1, 2, 1)
sns.countplot(heroes_data_cleaned["Alignment"])

#### code for right plot
plt.subplot(1, 2, 2)
sns.histplot(heroes_data_cleaned["Height"])
plt.xlim(0,500)

plt.show()
