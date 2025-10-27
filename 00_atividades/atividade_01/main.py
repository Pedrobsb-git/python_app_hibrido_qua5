# importaçãp de bibliotecas
import os

# Loop
while True:
    
    # Tratamento de exceção
        try:
            nome = input ("Informe seu nome: ").strip().title()
            email = input("Informe o e-mail: ").strip().lower()
            cpf = input("Informe o CPF: ").strip()
            telefone = input("Informe o seu Telefone: ").strip()

    # Limpeza de  console
            os.system("cls")

    # Saida de dados
            print(f"Nome: {nome}")
            print(f"E-mail: {email}")
            print(f"CPF: {cpf}")
            print(f"Telefone: {telefone}")
        except:
              print("Fim do Programa")