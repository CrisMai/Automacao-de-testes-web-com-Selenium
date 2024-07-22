from pages.carrinho_page import CarrinhoPage
from pages.login_page import LoginPage
from pages.home_page import HomePage # type: ignore
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_add_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"
        
        # Fazendo o login
        login_page.fazer_login("standart_user", "secret_sauce")

        # Adicionando a mochila ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando que a mochila foi adicionada
        home_page.accessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        
        # Clicando para voltar a tela de produtos
        carrinho_page.clicar_continuar_comprando()

        #  Adicionando mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        #  Verificando que os 2 produtos estão no carrinho
        home_page.accessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)
