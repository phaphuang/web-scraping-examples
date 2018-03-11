from selenium import webdriver

browser = webdriver.Chrome("C:\Anaconda2\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
browser.get("https://www.python.org/")
nav = browser.find_element_by_id("mainnav")
print(nav.text)
