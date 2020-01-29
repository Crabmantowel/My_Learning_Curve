# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = 7  # Counter for quantity of times to perform operation
while count != 0:  # Start of the big Cycle
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    position = 18  # Position of URL on the page to which Crawler will move
    for tag in tags:
        position -= 1
        if position == 0:
            url = tag.get('href', None)
            print(url)
            break
    count -= 1
