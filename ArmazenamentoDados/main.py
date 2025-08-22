# Dicionário com correspondência exata exigida pelos testes
armazenamento = {
    "Imagem": "Blob Storage",
    "Transações Bancárias": "Banco de Dados Relacional",
    "Logs de Servidor": "Data Lake",
    "Documentos Word": "SharePoint"
}

# Entrada do usuário
tipo_dado = input()  # Não colocar texto extra

# Saída exata
print(armazenamento[tipo_dado])
