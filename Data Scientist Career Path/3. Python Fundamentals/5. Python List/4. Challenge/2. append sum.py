#Write your function here

def append_sum(lst):
  lst.append(sum(lst[-2:]))
  lst.append(sum(lst[-2:]))
  lst.append(sum(lst[-2:]))
  return lst


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))