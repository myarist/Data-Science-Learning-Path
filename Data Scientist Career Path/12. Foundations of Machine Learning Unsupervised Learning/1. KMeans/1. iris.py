import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

print(iris)

print(iris.data)
print(iris.target)
print(iris.DESCR)