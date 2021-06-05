import requests

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(webpage, "html.parser")

print(soup)