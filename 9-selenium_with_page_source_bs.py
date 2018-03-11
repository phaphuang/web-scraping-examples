# chcp 65001
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://www.python.org/")
page = BeautifulSoup(browser.page_source,"html5lib")
links = page.findAll("a")
for link in links:
    print(link)
browser.close()
