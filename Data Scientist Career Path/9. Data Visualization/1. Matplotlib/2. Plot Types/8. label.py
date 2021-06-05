import codecademylib
from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct="%0.1f%%")
plt.axis('equal')
plt.legend(payment_method_names)

plt.show()