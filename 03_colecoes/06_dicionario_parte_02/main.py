# declarção de dicionário
usuario = { 
    'nome': "Alex Machado",
    'nascimento': "01/01/1985",
    'telefone': "(61)98765-4321",
    'enderoço': "QI",
    'email': "alex@gmail.com"
}
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")