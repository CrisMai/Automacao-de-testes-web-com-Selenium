import  time
from selenium  import webdriver

browser = webdriver.Chrome()

# get()
browser.get("https://www.saucedemo.com/")

# title
print("O titulo da pagina é:", browser.title)


# current_url
print("A URL da pagina é:", browser.current_url)


# page_source
print("O código fonte da pagina é:", browser.page_source)
