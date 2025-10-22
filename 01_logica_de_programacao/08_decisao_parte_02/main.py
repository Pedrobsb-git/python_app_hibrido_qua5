# declaração de variáveis
nome = input("Informe o seu nome: ").strip().title()
idade = int(input("Informe sua idade: ").strip())
altura = float(input("Informe a altura: ").strip().replace(",","."))

# verificação das condições
if idade >= 12 and altura >= 1.15:
    print(f"Entrada de {nome} Autorizada.")
else:
    print (f"Entrada de {nome} NÃO AUTORIZADA.")
    