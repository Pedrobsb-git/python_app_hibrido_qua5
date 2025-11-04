# declaração de dicionário
usuario = {}

# entrada de dados
usuario = {
    'nome': "Marcos Silva",
    'email': "marcossil@gmail.com",
    'telefone': "(61)98453-2005",
    'cpf': "321523784-01",
    'genero': "Masculino"
}

# exibir os dados
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")

# usuário escolhe o campo que deseja mudar
while True:
    campo = input("Informe o nome do campo que deseja alterar ou digite 'sair' para encerrar o programa: ").strip().lower()

    match campo:
        case "nome":
            usuario['nome'] = input("Informe o novo 'nome': ").strip()
        case "email":
            usuario['email'] = input("Informe o novo 'email': ").strip()
        case "telefone":
            usuario['telefone'] = int(input("Informe o novo 'telefone': ").strip())
        case "cpf":
            usuario['cpf'] = input("Informe o novo 'cpf': ").strip()
        case "genero":
            usuario['genero'] = input("Informe o novo 'genero': ").strip()
        case "sair":
            break
        case _:
            print("Valor Inválido.")
            continue
# mostra na tele os novos valore
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")