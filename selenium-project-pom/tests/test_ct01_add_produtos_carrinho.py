from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.home_page import HomePage # type: ignore
import conftest
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_add_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        
        # Fazendo o login
        login_page.fazer_login("standart_user", "secret_sauce")

        # Adicionando a mochila ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

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
