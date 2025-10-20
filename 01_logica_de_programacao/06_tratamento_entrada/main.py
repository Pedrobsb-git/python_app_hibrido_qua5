# declaração de variáveis
nome = input("Informe seu nome: ").strip().title() 
idade = int(input("informe sua idade: ").strip())
altura = float(input("Informe sua altura: ").strip().replace(",","."))

# saída de dados
print(f"Olá {nome}, seja bem vindo.")
print(f"Idade: {idade}")
print(f"Altura: {altura}")