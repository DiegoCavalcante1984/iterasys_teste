
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
    


#preenche os campos de login e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

#------------------------------------ Scenario Outline--------------------------------------------------- 
#preencher com usuario em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

#preencher com usuario ,mas senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login   

#clica no botao de login,sem usuario e senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
   context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login       

#--------------------------------------------------------------------------------------------------
#------------------------------------Outline com IF------------------------------------------------
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
    if senha != '<branco>':    
        context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login
        
#--------------------------------------------------------------------------------------------------------  
   
   
@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR,".title").text == "Products"


    # teardown / encerramento
    context.driver.quit() 
   
#válida o erro de senha
@then(u'o sistema exibe uma mensagem de erro')
def step_impl(context):
   assert context.driver.find_element(By.CSS_SELECTOR,"h3").text == 'Epic sadface: Username and password do not match any user in this service'
    
    
#válida o erro de senha para o Snario outline
@then(u'o sistema exibe uma {mensagem} de erro')
def step_impl(context, mensagem):
   assert context.driver.find_element(By.CSS_SELECTOR,"h3").text == mensagem
     
  