
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By



@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    #setup / inicialização
    context.driver = webdriver.Chrome() # instanciar o objeto do selenium webdriver com chrome
    context.driver.maximize_window() # maximiza a janela do navegador
    context.driver.implicitly_wait(10) # aguarda por até 10 sec qualquer elemento
    # passo
    
    context.driver.get("https://www.saucedemo.com")# abre o navegador no site alvo
    



@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login
    #time.sleep(4)
   
   
@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR,".title").text == "Products"
     

    # teardown / encerramento
    context.driver.quit() 
   

