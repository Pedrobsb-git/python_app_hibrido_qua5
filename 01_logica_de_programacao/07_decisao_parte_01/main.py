# declaração de variáveis
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe seu idade: ").strip())

# decisão
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")