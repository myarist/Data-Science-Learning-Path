import codecademylib
from matplotlib import pyplot as plt

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

# Make your plot here
plt.figure(figsize=(10, 8))
plt.hist(exam_scores1, bins=12, normed=True, histtype='step', linewidth=2)
plt.hist(exam_scores2, bins=12, normed=True, histtype='step', linewidth=2)

plt.legend(["1st Yr Teaching", "2nd Yr Teaching"])

plt.title("Final Exam Score Distribution")
plt.xlabel("Percentage")
plt.ylabel("Frequency")

plt.show()
plt.savefig('my_histogram.png')
