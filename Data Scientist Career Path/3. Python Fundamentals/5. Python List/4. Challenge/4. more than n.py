#Write your function here

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False


#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))