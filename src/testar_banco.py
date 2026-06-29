from conexao import criar_conexao, fechar_conexao

# Tenta abrir a conexão
minha_conexao = criar_conexao()

# Se a conexão foi bem-sucedida, fecha ela logo em seguida
if minha_conexao:
    fechar_conexao(minha_conexao)
else:
    print("Verifique se o seu servidor MySQL local está ativo e se os dados de login estão corretos.")
