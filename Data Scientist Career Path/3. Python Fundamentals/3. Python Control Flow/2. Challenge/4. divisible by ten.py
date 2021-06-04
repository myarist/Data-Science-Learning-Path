# Write your divisible_by_ten() function here:

def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else: 
    return False

# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False