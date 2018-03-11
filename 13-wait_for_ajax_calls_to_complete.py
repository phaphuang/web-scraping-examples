from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://resttesttest.com/")
browser.find_element_by_id("submitajax").click()

try:
    # check for div element text if it’s “HTTP 200 OK” with 10 seconds timeout, then we save the result page
    # EC.url_changes() - URL change using
    # EC.new_window_is_opened() - New opened window using
    # EC.title_is() - Changes in title using
    element = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "statuspre"), "HTTP 200 OK"))
finally:
    browser.get_screenshot_as_file("image.png")
browser.close()
