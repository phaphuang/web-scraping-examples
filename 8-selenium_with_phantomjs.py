from selenium import webdriver

browser = webdriver.PhantomJS("C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
browser.get("https://www.python.org/")
print(browser.find_element_by_class_name("introduction").text)
print(browser.find_elements_by_id("id"))
browser.close()
