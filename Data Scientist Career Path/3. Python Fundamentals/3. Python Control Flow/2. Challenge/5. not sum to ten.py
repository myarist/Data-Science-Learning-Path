# Write your not_sum_to_ten function here:

def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False
  
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False