Feature:Selecionar Produto

    Scenario:Selecionar produto 'Sauce Labs Backpack'
    Given que acesso o site sauce Demo 
    When preencho os campos de login com usuario standard_user e senha secret_sauce
    Then sou direcionado para pagina Home 
