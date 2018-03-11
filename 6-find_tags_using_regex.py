from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

try:
    html = urlopen("https://www.python.org/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")

    tags = res.findAll("img", {"src": re.compile("\.\./uploads/photo_.*\.png")})

    for tag in tags:
        print(tag.getText())
