import xml.etree.ElementTree as ET  # ET is a shortcut to module
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_218968.xml'
html = urlopen(url, context=ctx).read()
soup = str(BeautifulSoup(html, "html.parser"))

xml_doc = ET.fromstring(soup)
comments = xml_doc.findall('comments/comment')
commentssum = 0
for comment in comments:
    print('Name: ', comment.find('name').text)
    print('Count: ', comment.find('count').text)
    commentssum += int(comment.find('count').text)
print(commentssum)
