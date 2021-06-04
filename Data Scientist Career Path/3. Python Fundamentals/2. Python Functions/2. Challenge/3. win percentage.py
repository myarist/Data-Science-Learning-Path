# Write your win_percentage function here:

def win_percentage(wins, losses):
  total = wins + losses
  win_ratio = wins / total
  win_percentage = win_ratio * 100
  return win_percentage

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100