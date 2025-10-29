# declaração de Lista
nomes = ["Fulano", "Ciclano", "Beltrano", "João", "Maria", "José"]

# exibe o primeiro nome
print ("nomes" [0])

# ordene a lista em ordem alfabética
nomes.sort()

# re-exibe a lista em ordem alfabética
print("\nOrdem Alfabética:\n")
for nome in nomes:
    print(nome)

# reverte a ordem da lista
nomes.sort(reverse=True)

print("\nOderm alfabética reversa:\n")
for nome in nomes:
    print(nome)
    