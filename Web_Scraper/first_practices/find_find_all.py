#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

# Using those modules to get an HTML version of this URL
url = 'https://www.scrapethissite.com/pages/simple/'
request = requests.get(url)

# Check if the request is successful
if request.status_code == 200:
    # Pass the page content to BeautifulSoup
    soup = BeautifulSoup(request.text, 'html.parser')
    soup_links = soup.find_all('a')
    for links in soup_links:
        print("Class : ", links.get('class'))
        print("Link : ", links.get('href'))
    
else:
    print(f"Failed to retrieve the page. Status code: {request.status_code}")


