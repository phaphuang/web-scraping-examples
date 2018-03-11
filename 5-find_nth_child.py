from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.python.org/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")

    tags = res.span.findAll("a")
    # gets the nav element with id “site-navigation”
    tags = res.find("nav", {"id": "site-navigation"}).select("a")[3]

    for tag in tags:
        print(tag.getText())
