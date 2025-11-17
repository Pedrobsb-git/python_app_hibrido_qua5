from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from entidades import criar_tb_pessoa
from modulo import limpar

def main():
    enegine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(enegine, Base)
    Session = sessionmaker(bind=enegine)
    session = Session()

    limpar()
    # TODO: fazer o CRUD

    session.close()

if __name__ == "__main__":
    main()