# Write your in_range function here:

def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False

# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False