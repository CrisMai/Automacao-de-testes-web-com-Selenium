import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # type: ignore


class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name'and text()='{}']")

    def verificar_produto_carrinho_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)