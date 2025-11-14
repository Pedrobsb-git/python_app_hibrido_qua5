import os

from classes import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
   limpar()

   usuario = PessoaFisica(
   nome="",
   idade=0,
   cpf="",
   profissao="",
   emai="",
   telefone="",
   endereco=""
    )
   empresa = PessoaJuridica(
       nome_fantasia="",
       cnpj="",
       website="",
       email="",
       telefone="",
       endereco=""
    )
   
    print("INFORME OS DADOS DO USUÁRIO:\n")
   
   def main():
      empresa.nome_fantasia = input("Informe o Nome: ").strip().title()
      empresa.cnpj = input("Informe o CNPJ: ").strip()
      empresa.website = input("Informe a URL do Website: ").strip().title()
      empresa.email = input("Informe o E-mail: ").strip().lower()
      empresa.telefone = input("Informe o Telefone: ").strip()
      empresa.endereco = input("Informe o Endereço: ").strip.title()

if __name__ == "__main__":
    main()