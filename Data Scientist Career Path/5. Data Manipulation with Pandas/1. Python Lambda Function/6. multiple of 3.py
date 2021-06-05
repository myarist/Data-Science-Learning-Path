#Write your lambda function here
multiple_of_three = lambda num: "multiple of three" if num % 3 == 0 else "not a multiple"

print(multiple_of_three(9))
print(multiple_of_three(10))
