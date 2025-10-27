# importação de bibliotecas
import os
import math

# Loop
while True:
    
     # Limpeza de console
        os.system("cls")

    #tratamento de exceção
   try:
        nome = input ("Informe o nome: ").strip().title()
        email = input("Informe o e-mail: ").strip().lower()
        cpf = input("Informe o CPF: ").strip()

     #Limpeza de console
        os.system("cls")

     # saida de dados
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

     #menu
        print("1 - Iserir novos dados.")
        print("2 - Sair do programa.")

        opcao = input("Opção deseja: ").strip()
        
     # verificação a opção escolhida
        math, opcao:
         case "1":
           continue
         case "2":
            print("Programa encerrado.")
            break
         case _:
            print("Opção inválida.")
            break
   except:
      print("Não foi possivel receber informações.")