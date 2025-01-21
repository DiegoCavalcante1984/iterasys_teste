#bibliotécas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#classe
class Test_Produtos():

# atributos 
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
        self.driver.find_element(By.ID,("login-button")).click() #clica no botão

        # transição de tela 

        assert self.driver.find_element(By.CSS_SELECTOR, ("span.title")).text == "Products" #confirma se é a pagina de produtos
        assert self.driver.find_element(By.ID,("item_4_title_link")).text == "Sauce Labs Backpack" # confirma o produto selecionado
        assert self.driver.find_element(By.CSS_SELECTOR,(".inventory_item_price:nth-child(1)")).text == "$29.99" # confirma o preço do produto
        self.driver.find_element(By.ID,("add-to-cart-sauce-labs-backpack")).click() #diciona o item ao carrinho
        assert self.driver.find_element(By.CSS_SELECTOR,("span.shopping_cart_badge")).text == "1" #confirma se o item está na quantidade certa no carrinho no icone
        self.driver.find_element(By.CSS_SELECTOR,("a.shopping_cart_link")).click()# clica no carrinho
        assert self.driver.find_element(By.CSS_SELECTOR,("span.title")).text == "Your Cart"#confirma se está na página do carrinho
        assert self.driver.find_element(By.CSS_SELECTOR,("[data-test='item-quantity']")).text == "1" # confirma a quantidade
        assert self.driver.find_element(By.ID,("item_4_title_link")).text == "Sauce Labs Backpack" #confirma o produto
        assert self.driver.find_element(By.CSS_SELECTOR,(".inventory_item_price:nth-child(1)")).text == "$29.99" #confirma o preço
        self.driver.find_element(By.ID,("remove-sauce-labs-backpack")).click()#remove o item do carrinho
        self.driver.find_element(By.ID,("react-burger-menu-btn")).click() #clica no menu
        self.driver.find_element(By.ID,("logout_sidebar_link")).click()#clica na link logout