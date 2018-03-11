from selenium import webdriver

browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://likegeeks.com/")
print(browser.get_cookies())
browser.delete_all_cookies()
browser.close()
