import random
#Write your lambda function here
add_random = lambda num: num + random.randint(1,10)

print(add_random(5))
print(add_random(100))