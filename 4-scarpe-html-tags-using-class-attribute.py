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

    tags = res.findAll("h2", {"class": "widget-title"})
    # To filter a list of tags
    tags = res.findAll("span", "a" "img")
    # extract tags that have these classes
    tags = res.findAll("a", {"class": ["url", "readmorebtn"]})
    # content based on the inner text itself using the text argument
    tags = res.findAll(text="Python Programming Basics with Examples")

    for tag in tags:
        print(tag.getText())
