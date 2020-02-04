import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_218969.json'  # input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
userlist = json.loads(str(soup))
sum_of_comments = int()
for user in userlist["comments"]:
    #  print('User: ', user["name"])
    #  print('Comment count: ', int(user["count"]))
    sum_of_comments += user["count"]
print(sum_of_comments)
