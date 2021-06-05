import codecademylib
from matplotlib import pyplot as plt

x = range(6)
y1 = [1, 2, 3, 4, 5, 6]
y2 = [-1, 1, 3, 4, 4, 4]

plt.plot(x, y1, marker='o', color='pink')
plt.plot(x, y2, marker='o', color='gray')

plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(["Y1","Y2"], loc=4)

plt.show()