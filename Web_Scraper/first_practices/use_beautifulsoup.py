#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

# Using those modules to get an HTML version of this URL
url = 'https://www.scrapethissite.com/pages/simple/'
request = requests.get(url)

# Print the response headers to check for redirects or content type issues
print(f"Response Headers: {request.headers}")

# Check if the request is successful
if request.status_code == 200:
    # Print the raw content of the page to see if it contains HTML
    print("Page Content:", request.text[:500])  # Only print the first 500 characters to avoid flooding the terminal
    
    # Pass the page content to BeautifulSoup
    soup = BeautifulSoup(request.text, 'html.parser')
    
    # Print out the parsed HTML (to see if BeautifulSoup is working)
    print(soup.prettify())  # prettify() helps format the output for readability
else:
    print(f"Failed to retrieve the page. Status code: {request.status_code}")
