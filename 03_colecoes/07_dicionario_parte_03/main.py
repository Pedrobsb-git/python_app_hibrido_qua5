# declaração de dicionário
veiculo = {
    'fabricante': "Chevrolet",
    'modelo': "Chevette",
    'ano': 1973,
    'cor': "branco",
    'placa': "DF-1973"
}

# exibir os dados
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

# usuário escolhe o campo que deseja mudar
while True:
    campo = input("Informe o nome do campo que deseja alterar ou digite 'sair' para encerrar o programa: ").strip().lower()

    match campo:
        case "fabricante":
            veiculo['fabricante'] = input("Informe o novo valor da 'fabricante': ").strip()
        case "modelo":
            veiculo['modelo'] = input("Informe o novo valor da 'modelo': ").strip()
        case "ano":
            veiculo['ano'] = int(input("Informe o novo valor da 'ano': ").strip())
        case "cor":
            veiculo['cor'] = input("Informe o novo valor da 'cor': ").strip()
        case "placa":
            veiculo['placa'] = input("Informe o novo valor de 'placa': ").strip()
        case "sair":
            break
        case _:
            print("Valor Inválido.")
            continue
# mostra na tele os novos valore
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")