#Write your function here

def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    lst[index] *= 2
  return lst


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))