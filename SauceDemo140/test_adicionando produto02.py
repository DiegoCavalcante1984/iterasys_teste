#bibliotécas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#classe
class Test_Produtos():

#atributos 
    url = "https://www.saucedemo.com"

#funções e métodos

    def setup_method(self, method):                     # método de inicialização dos testes
        self.driver = webdriver.Chrome()              # instânciar o objeto do selenium webdriver
        self.driver.implicitly_wait(10)           # define o tempo de espera padrão por elementos em 10 seg
        
                                                  
                                                    

    def teardown_method(self, method):                    # método de finalização
        self.driver.quit()                              # encerra/ destrói o selenium webdriver

    def test_incluir_Produtos(self):   # método de teste
        self.driver.get(self.url)  
        self.driver.find_element(By.ID, ("user-name")).send_keys("standard_user") # escreve o campo username
        self.driver.find_element(By.ID,("password")).send_keys("secret_sauce")    # escreve no campo senha    

