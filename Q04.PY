login_padrao = "admin"
senha_padrao = "123"
login = input("digite seu login: ")
senha = input("digite sua senha: ")
if login == login_padrao and senha_padrao == senha:
    print("olá admin, seja bem-vindo!")
else:
    print("login ou senha incorretos, tente novamente.")