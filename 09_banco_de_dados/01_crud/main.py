from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from entidades import criar_tb_pessoa
from modulo import limpar, cadastrar, listar, atualizar, deletar

def main():
    enegine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(enegine, Base)
    Session = sessionmaker(bind=enegine)
    session = Session()

    limpar()
    while True:
        print(f"{'-'*20} 🍎 CRUD DA COBRA 🍎 {'-'*20}\n")
        print("0 - Sair do programa")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas")
        print("3 - Atualizar Dados")
        print("4 - Excluir pessoa")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
                case "0":
                    print("Programa encerrado.")
                    break
                case "1":
                    print(cadastrar(session, Pessoa))
                    continue
                case "2":
                    listar(session, Pessoa)
                    continue
                case "3":
                    print(atualizar(session, Pessoa))
                    continue
                case "4":
                    print(deletar(session, Pessoa))
                    continue
                case _:
                    print("Opção Invalida.")
                    continue
        session.close()
    if __name__ == "__main__":
            main()