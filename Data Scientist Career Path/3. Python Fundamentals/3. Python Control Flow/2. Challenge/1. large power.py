# Write your large_power function here:

def large_power(base, exponent):
  res = base ** exponent

  if res > 5000:
    return True
  else:
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False