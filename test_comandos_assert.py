# O assert sempre verifica se o retorno da condição é true
assert True

# assert numbers
num_esperado = 2
num_obtido = 2
assert num_esperado == num_obtido, f"Esperado{num_esperado}. Atual{num_obtido}."

# assert text
text_esperado = "Selenium Webdriver"
text_obtido = "Selenium webdriver"
assert text_esperado.lower() == text_obtido.lower(), f"Esperado{text_esperado}. Atual{text_obtido}."

# assert text in string
text_esperado = "Selenium"
text_obtido = "Selenium webdriver"
assert text_esperado in text_obtido, f"Esperado{text_esperado}. Atual{text_obtido}."

