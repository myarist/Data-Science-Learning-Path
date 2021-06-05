import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import codecademylib3

pie_data = pd.read_csv("pie_data.csv")

graph_counts = pie_data["values"]

graph_labels = pie_data["labels"]

plt.subplot(1,2,1)
plt.pie(graph_counts, labels = graph_labels)
plt.axis('Equal')
plt.title("Tough to Compare")

plt.subplot(1,2,2)
sns.barplot(graph_labels, graph_counts)
plt.title("Easy to Compare")

plt.show()
