# bibliotecas
import os

# declaração de lista
usuarios = []

# Limpa console
os.system("cls")

while True:
    # menu
    print("1 - Cadastrar Novo Usuário")
    print("2 - Listar Usuários")
    print("3 - Sair do Programa")
    opcao = input("Informe a opção deseja: ").strip()
    match opcao:
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe o nome do Usuário: ").strip().title()
            usuario['idade'] = int(input("Informe a idade do Usuário: ").strip())
            usuario['email'] = input("Informe o e-mail do Usuário: ").strip().lower()
            usuarios.append(usuario)
            os.system("cls")
            print("Novo usuário inserido com sucesso.")
            continue           
        case "2":
            for usuario in usuarios:
                for chave in usuario:
                    print(f"{chave.capitalizer()}: usuario[chave]}")
                print(f"{'-'*40}")
            continue
        case "3":
            break
        case _:
            print("Opção Inválida.")
            continue