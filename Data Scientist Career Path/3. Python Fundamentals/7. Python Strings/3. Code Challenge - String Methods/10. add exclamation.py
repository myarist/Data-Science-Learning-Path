# Write your add_exclamation function here:
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn