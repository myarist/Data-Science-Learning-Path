import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import codecademylib3

major_data = pd.read_csv("major_data.csv")
print(major_data.head())

major_data_agg = pd.read_csv("major_data_agg.csv")
print(major_data_agg.head())

pie_wedges = major_data["proportion"]
pie_labels = major_data["major"]

pie_wedges_agg = major_data_agg["proportion"]
pie_labels_agg = major_data_agg["department"]

plt.subplot(2,1,1)
plt.pie(pie_wedges, labels = pie_labels)
plt.axis('Equal')
plt.title("Too Many Slices")
plt.tight_layout()

plt.subplot(2,1,2)
plt.pie(pie_wedges_agg, labels = pie_labels_agg)
plt.axis('Equal')
plt.title("Good Number of Slices")
plt.tight_layout()

plt.show()

