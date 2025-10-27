# tratamento de exceção
try:
    nome = input("Informe o nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())

    # Lista de filmes
    sala_1 = "A Roda Quadrada"
    sala_2 = "A Volta dos que Não foram"
    sala_3 = "Poeira em alto mar"
    sala_4 = "As tranças do Rei careca"
    sala_5 = "A Vingaça do frango assado"
    
    # Classificação dos Filmes
    while True:
        print(f"Sala 1 - {sala_1} - CLACIFICAÇÃO LIVRE")
        print(f"Sala 2 - {sala_2} - CLACIFICAÇÃO 12 ANOS")
        print(f"Sala 3 - {sala_3} - CLACIFICAÇÃO 14 ANOS")
        print(f"Sala 4 - {sala_4} - CLACIFICAÇÃO 16 ANOS")
        print(f"Sala 5 - {sala_5} - CLACIFICAÇÃO 18 ANOS")
        sala = input ("Informe a sala desejada: ").strip()

        # verifica a sala selecionada
        match sala:
            case "1":
                filme = sala_1
                idade_minima = 0
            case "2":
                filme = sala_2
                idade_minima = 12
            case "3":
                filme = sala_3
                idade_minima = 14
            case "4":
                filme = sala_4
                idade_minima = 16
            case "5":
                fime = sala_5
                idade_minima = 18
            case _:
                print ("Sala inexistente.")
        if idade >= idade_minima:
            print(f"{nome} escolheu {filme}. Tenha uma bom filme!")
            break
        else:
            print(f"{nome} não foi autorizado a ver {filme}.")
            continue
except Exception as e:
    print (f"Erro no programa. {e}")