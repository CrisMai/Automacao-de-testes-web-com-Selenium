import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):

        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        # Faz login
        login_page.fazer_login("standart_user", "senha_incorreta")
        
        # Verificar se o login não foi realizado e a mensagem de erro apareceu
        login_page.verificar_mensagem_erro_login()    