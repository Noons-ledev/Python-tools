#!/usr/bin/python3
"""
This module will introduce the v1 of waiting for user URL to parse links on the HTML page of that given URL
"""
from bs4 import BeautifulSoup
import requests


url = input("url please ?")

try:
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html.parser')
        soup_texts = soup.find_all('p')
        for text in soup_texts:
             print(text.prettify())
    else:
            print("Request did not pass, statuscode: {}".format(request.status_code))

except requests.exceptions.RequestException:
    print("URL not accessible")