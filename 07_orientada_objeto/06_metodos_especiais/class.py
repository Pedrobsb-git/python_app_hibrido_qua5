class Pessoa:
    # construtor
        def __init__ (self, nome, idade, genero, telefone):
                self.__nome = nome
                self.__idade = idade
                self.__genero = genero
                self.__telefone = telefone

        # metodos especiais
        def __str__ (self):
            return f"Olá, meu nome é {self.__nome}, tenho {self.__idade} anos,
            sou do genero é {self.__genero} e meu telefone é {self.__telefone}."

        def __len__(self):
            return self.__idade
          
class Pessoa:
       @property
       def telefone(self):
           return self.__telefone

       @telefone.setter
       def telefone(self, telefone):
           self.__telefone = telefone                 