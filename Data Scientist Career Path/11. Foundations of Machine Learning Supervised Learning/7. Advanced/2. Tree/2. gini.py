from collections import Counter

labels = ["unacc", "unacc", "acc", "acc", "good", "good"]
#labels = ["unacc","unacc","unacc", "good", "vgood", "vgood"]
#labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc"]

impurity = 1
label_counts = Counter(labels)
for label in label_counts:
  probability_of_label = label_counts[label]/len(labels)
  impurity -= probability_of_label ** 2
  
print(impurity)