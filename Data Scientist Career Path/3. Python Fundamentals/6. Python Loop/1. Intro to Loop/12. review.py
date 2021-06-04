# Your code below:

single_digits = list(range(10))

squares = []

for i in single_digits:
  print(i)
  squares.append(i ** 2)
print(squares)

cubes = [x ** 3 for x in single_digits]

print(cubes)