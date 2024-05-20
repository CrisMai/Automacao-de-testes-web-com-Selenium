Automação de testes web com Selenium Webdriver e Python.


*** Configurando o Ambiente ***

* Baixando e instalando o Python

Acesse o site https://www.python.org
Na aba de Downloads baixe a versão disponível
Para conferir se foi instalado corretamente acesse o prompt de comando e digite python --version


* Baixando e instalando o Pycharm

Acesse o site https://www.jetbrains.com/
Na aba Developer Tools clique na opção PyCharm e baixe a versão Community


*** Criando Ambiente Virtual (venv) no Vs Code ***

Acesse o terminal do Vs Code e entre na pasta que deseja criar o projeto
Use o comando: python -m venv venv (nome do ambiente virtual)
Entre na pasta onde o projeto foi criado e certifique-se que o ambiente virtual foi criado
Em seguida ative o ambiente virtual usando o código: venv\Scripts\Activate.ps1
Caso ocorra um erro no momento da ativação do script do ambiente virtual rode o seguinte comando: 
Set-ExecutionPolicy Unrestricted -Scope Process
Esse comando vai habilitar a execução do script na sessão aberta do Powershell.



*** Criando Ambiente Virtual (venv) no PyCharm ***

Acesse o PyCharm e crie um novo projeto
Escolha o caminho da pasta onde o projeto ficará 
O PyCharm assim que você criar um novo projeto ele já cria um novo ambiente virtual
Clica em Create
Em seguida ative o ambiente virtual usando o código: venv\Scripts\Activate.ps1


*** Configurando o Selenium Webdriver ***

Acesse https://www.selenium.dev/
Clica em downloads e clica na versão do Selenium para Python
Copia o seguinte comando: pip install selenium
Cola o comando no PyCharm ou no Vs Code e aguarde a instalação
Para verificar se foi realmente instalado use o comando: 
pip show selenium


