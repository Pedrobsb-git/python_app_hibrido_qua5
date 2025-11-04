# função principal
def main():
    # entrada de dados
    nome = input("Informe seu Nome: ").strip().title()
    idade = int(input("Informe sua Idade: ").strip())

    # operador ternário
    resultado = "é maior de idade." if idade >= 18 else "é menor de idade"

    # saída de dados
    print(f"{nome} {resultado}")

# protege algoritimo principal
if __name__ == "__main__":
 main()