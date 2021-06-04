# Write your count_char_x function here:

def count_char_x(word,x):
  count = 0
  for i in word:
    if i == x:
      count += 1
  return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1