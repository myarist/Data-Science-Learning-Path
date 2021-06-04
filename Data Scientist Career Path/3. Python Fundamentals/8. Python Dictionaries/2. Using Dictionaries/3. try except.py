caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level.update({"matcha":30})

try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")