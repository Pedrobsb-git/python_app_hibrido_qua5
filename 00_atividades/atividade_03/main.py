# bibliotecas
import math

# tratamento de exceção
try:
    # entrada de dados
    nome = input("Informe o nome: ").strip().title()
    peso = float(input("Informe seu peso em kg: ").strip().replace(",","."))
    altura = float(input("Informe sua altura em metros: ").strip().replace(",","."))

    # cáculo do IMC
    imc = peso/(altura**2)
    
    # exibe o IMC do usuario 
    print(f"{nome}, seu IMC é {imc:.2f}")

    #diagnostico do IMC
    if imc < 18.5:
        print(f"{nome} está abaixo do peso.")
    elif imc < 25:
        print(f"{nome} está no peso idaeal.")
    elif imc < 30:
        print(f"{nome} está acima do peso.")
    elif imc < 35:
        print(f"{nome} está obeso.")
    elif imc < 40:
        print(f"{nome} está com obesidade nivel II.")
    else:
        print(f"{nome} está com obesidade morbida.")
except:
    print(f"ERRO! {e}")