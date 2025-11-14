import os

from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "int" else "clear")

def main():
    pessoa.name = input("Informe o Nome: ").strip().title()
    pessoa.idade = int(input("Informe a sua Idade: ").strip())
    pessoa.genero = input("Informe seu gênero: ").strip().lower()
    pessoa.telefone = input("Informe seu telefone: ").strip()

    # saída de dados
    print(pessoa)
    print(f"idade: {len(pessoa)}")
if __name__ == "__main__":
    main()