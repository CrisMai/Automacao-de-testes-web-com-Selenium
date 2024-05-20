import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.google.com")
time.sleep(5)