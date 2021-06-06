import re

headline_one = '<h1>Nation\'s Top Pseudoscientists Harness High-Energy Quartz Crystal Capable Of Reversing Effects Of Being Gemini</h1>'

tweet = '@fat_meats, veggies are better than you think.'

headline_no_tag = re.sub(r'<.?h1>', '', headline_one)

tweet_no_at = re.sub(r'@', '', tweet)

try:
  print(headline_no_tag)
except:
  print('No variable called `headline_no_tag`')
try:
  print(tweet_no_at)
except:
  print('No variable called `tweet_no_at`')