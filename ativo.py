from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_base import SeleniumBase


class Ativo(SeleniumBase):
    """
    Classe para representar um ativo financeiro e coletar seus dados econômicos usando Selenium.

    Args:
        asset_code (str): O código do ativo financeiro.
        headless (bool, optional): Define se o navegador deve ser executado em modo headless (sem interface gráfica).
                                   O padrão é True.

    Attributes:
        asset_code (str): O código do ativo financeiro.
        dados (dict): Um dicionário para armazenar os dados econômicos coletados.

    Methods:
        extrair_dados_de_linha(colunas): Extrai dados de uma linha de tabela.
        buscar_dados_economicos(): Inicia o driver Selenium, acessa o site Fundamentus, insere o código do ativo e coleta dados econômicos.
        extrair_dados_da_tabela(tabela): Extrai dados da tabela de detalhes do ativo.

    """

    def __init__(self, asset_code, headless=True):
        """
        Inicializa um objeto Ativo.

        Args:
            asset_code (str): O código do ativo financeiro.
            headless (bool, optional): Define se o navegador deve ser executado em modo headless (sem interface gráfica).
                                       O padrão é True.
        """
        super().__init__(headless)
        self.asset_code = asset_code
        self.dados = {}

    def extrair_dados_de_linha(self, colunas):
        """
        Extrai dados de uma linha da tabela de detalhes do ativo.

        Args:
            colunas (list): Uma lista de elementos de coluna da tabela.

        Returns:
            dict: Um dicionário com os dados extraídos.

        """
        if len(colunas) == 4:
            titulo_1 = colunas[0].text
            valor_1 = colunas[1].text
            titulo_2 = colunas[2].text
            valor_2 = colunas[3].text
            return {
                titulo_1: valor_1,
                titulo_2: valor_2
            }
        else:
            return {}

    def buscar_dados_economicos(self):
        """
        Inicia o driver Selenium, acessa o site Fundamentus, insere o código do ativo e coleta dados econômicos.

        """
        self.iniciar_driver()
        try:
            self.driver.get('https://www.fundamentus.com.br/detalhes.php')
            asset_input = self.buscar_elemento_por_xpath("//input[@name='papel']")
            asset_input.send_keys(self.asset_code)
            asset_input.send_keys(Keys.ENTER)
            tabela = self.buscar_elemento_por_xpath("//table[@class='w728']")
            self.dados = self.extrair_dados_da_tabela(tabela)
        finally:
            self.encerrar_driver()

    def extrair_dados_da_tabela(self, tabela):
        """
        Extrai dados da tabela de detalhes do ativo.

        Args:
            tabela: O elemento da tabela de detalhes do ativo.

        Returns:
            dict: Um dicionário com os dados extraídos.

        """
        dados = {}
        linhas = tabela.find_elements(By.TAG_NAME, "tr")
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            item = self.extrair_dados_de_linha(colunas)
            dados.update(item)
        return dados
