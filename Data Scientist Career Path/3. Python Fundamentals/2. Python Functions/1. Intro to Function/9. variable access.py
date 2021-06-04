# This function will print a hardcoded count of how many locations we have.
def print_count_locations():
    favorite_locations = "Paris, Norway, Iceland"
    print("There are 3 locations")
    return favorite_locations
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + print_count_locations())

print_count_locations()
show_favorite_locations()