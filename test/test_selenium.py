import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TesteDescontoVeiculos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Usando o webdriver do Chrome
        self.driver.get("http://localhost:3000")  # URL onde o site está rodando

    def test_cases(self):
        driver = self.driver

        # Definição dos casos de teste
        casos_de_teste = [
            {"descricao": "Hatch entre 2012 e atual", "tipo": "hatch", "ano": "2014", "saida": "10"},
            {"descricao": "Hatch entre 2007 e 2011", "tipo": "hatch", "ano": "2009", "saida": "15"},
            {"descricao": "Hatch antes de 2007", "tipo": "hatch", "ano": "2004", "saida": "19"},
            {"descricao": "Hatch ano de borda 1990", "tipo": "hatch", "ano": "1990", "saida": "19"},
            # # Adicionar mais casos de teste conforme necessário
            # {"descricao": "Valor do tipo de carro inválido", "tipo": "A", "ano": "2012", "saida": "-1"},
            # {"descricao": "Valor nulo para ano", "tipo": "hatch", "ano": "", "saida": "-2"},
        ]

        for caso in casos_de_teste:
            with self.subTest(caso=caso["descricao"]):
                # Seleciona o tipo de carro
                select_tipo = Select(driver.find_element(By.TAG_NAME, "select"))
                select_tipo.select_by_value(caso["tipo"])

                # Insere o ano do veículo
                ano_input = driver.find_element(By.XPATH, "//input[@type='number']")
                ano_input.clear()
                ano_input.send_keys(caso["ano"])

                # Clica no botão de calcular desconto
                calcular_btn = driver.find_element(By.TAG_NAME, "button")
                calcular_btn.click()

                # Verifica o desconto aplicado (resultado)
                result_element = driver.find_element(By.CLASS_NAME, "result")
                result_text = result_element.text

                # Valida a saída esperada
                self.assertIn(f"O desconto aplicado é de {caso['saida']}%", result_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()