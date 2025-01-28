#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
#Using those modules to get a HTML version of this URL
url = 'https://www.scrapethissite.com/pages/simple/'
request = requests.get(url)
print(request)
if request.status_code == 200:
    page = request.content
    
soup = BeautifulSoup(page, 'html.parser')
print(soup)
