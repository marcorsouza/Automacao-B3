from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumBase:
    def __init__(self, headless=True):
        self.headless = headless
        self.driver = None

    def iniciar_driver(self):
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def encerrar_driver(self):
        if self.driver:
            self.driver.quit()

    def aguardar_elemento_presente(self, by, value, timeout=10):
        if self.driver:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )

    def buscar_elemento_por_xpath(self, xpath, timeout=10):
        return self.aguardar_elemento_presente(By.XPATH, xpath, timeout)