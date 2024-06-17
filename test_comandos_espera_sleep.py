import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar o driver do navegador (por exemplo, Chrome)
driver = webdriver.Chrome()

# Navegar para uma URL
driver.get("http://www.saucedemo.com")

# Esperar 5 segundos para garantir que a página foi completamente carregada
time.sleep(5)

# Localizar o elemento pelo ID e clicar nele
button = driver.find_element(By.ID, "submit_button")
button.click()

# Esperar mais 5 segundos para observar o resultado do clique
time.sleep(5)

# Fechar o navegador
driver.quit()