import  time
from selenium  import webdriver

browser = webdriver.Chrome()

# get()
browser.get("https://google.com")


# maximize_window()
browser.maximize_window()
time.sleep(3)


# refresh
browser.refresh()
time.sleep(3)


# back
browser.get("https://www.saucedemo.com/")

browser.back()
time.sleep(3)


# forward
browser.forward()
time.sleep(3)


# close
browser.switch_to.new_window("tab")
time.sleep(3)

browser.close()


# quit
browser.switch_to.new_window("tab")
time.sleep(3)
browser.switch_to.new_window("tab")
time.sleep(3)

browser.quit()
