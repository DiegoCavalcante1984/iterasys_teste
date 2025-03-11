Feature:Selecionar Produto

    Scenario:Selecionar produto 'Sauce Labs Backpack'
        Given que acesso o site sauce Demo 
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home 

    Scenario:Login com a senha invalida
        Given que acesso o site sauce Demo
        When preencho os campos de login com usuario standard_user e senha laranja
        Then o sistema exibe uma mensagem de erro
    
   
    Scenario Outline:Login negativo
        Given que acesso o site sauce Demo
        When preencho os campos de login com usuario <usuario> e senha <senha>
        Then o sistema exibe uma <mensagem> de erro

        Examples:
        | usuario       | senha        | mensagem                                                                 |
        | standard_user | laranja      | Epic sadface: Username and password do not match any user in this service|
        | standard_user |              | Epic sadface: Password is required                                       |
        |               | secret_sauce | Epic sadface: Username is required                                       |
        | juca          | secret_sauce | Epic sadface: Username and password do not match any user in this service|
        | juca          | laranja      | Epic sadface: Username and password do not match any user in this service|
        | juca          |              | Epic sadface: Password is required                                       |
        |               |              | Epic sadface: Username is required                                       |
        |               | laranja      | Epic sadface: Username is required                                       |



    Scenario Outline:Login negativo com IF
        Given que acesso o site sauce Demo
        When digito os campos de login com usuario <usuario> e senha <senha> com IF
        Then o sistema exibe uma <mensagem> de erro

        Examples:
        | usuario       | senha        | mensagem                                                                 |
        | standard_user | laranja      | Epic sadface: Username and password do not match any user in this service|
        | standard_user | <branco>     | Epic sadface: Password is required                                       |
        | <branco>      | secret_sauce | Epic sadface: Username is required                                       |
        | juca          | secret_sauce | Epic sadface: Username and password do not match any user in this service|
        | juca          | laranja      | Epic sadface: Username and password do not match any user in this service|
        | juca          | <branco>     | Epic sadface: Password is required                                       |
        | <branco>      | <branco>     | Epic sadface: Username is required                                       |
        | <branco>      | laranja      | Epic sadface: Username is required                                       |