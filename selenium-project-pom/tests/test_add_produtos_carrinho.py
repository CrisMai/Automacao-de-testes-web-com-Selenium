from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Fazendo o login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Adicionando a mochila ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name'and text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH, "//*[text()='Add to card']").click()

# Verificando que a mochila foi adicionada
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# Clicando para voltar a tela de produtos
driver.find_element(By.Id, "continue-shopping").click()

#  Adicionando mais um produto ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name'and text()='Sauce Labs Bike Light']").click()
driver.find_element(By.XPATH, "//*[text()='Add to card']").click()

#  Verificando que os 2 produtos estão no carrinho
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
