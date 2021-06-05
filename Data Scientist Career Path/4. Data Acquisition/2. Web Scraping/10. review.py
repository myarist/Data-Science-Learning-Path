import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them"
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  
  stats = turtle.find("ul")
  stats_text = stats.get_text("|")
  turtle_data[turtle_name] = stats_text.split("|")

turtle_df = pd.DataFrame(turtle_data)



