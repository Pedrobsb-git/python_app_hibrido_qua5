from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str

    def __str__(self):
        return f"E-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    
@dataclass
class PessoaFisica(Pessoa):
    nome: str
    idade: int
    cpf: str
    profissao: str

    def __str__(self):
        return f"\nDados do Usuário:\nNome: {self.nome}\nIdade: {len(self)} \nCPF: {self.cpf}\n{super().__str__()}"
    
    def __len__(self):
        return self.idade
    
@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str

    def __str__(self):
        return f"Dados da Empresa:\nNome da empresa: {self.nome_fantasia}\nCNPJ: {self.cnpj}\nWebsite: {self.website}\n{super().__str__()}"