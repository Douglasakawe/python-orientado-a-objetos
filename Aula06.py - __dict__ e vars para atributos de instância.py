class Pessoa:
    ano_atual = 2022

    def init(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
#p1.nome = 'EITA'
#print(p1.home)
#p1.dict['outra'] = 'coisa'
#p1.dict['nome'] = 'EITA'
#del p1.dict['nome']
#print(p1.dict)
print(vars(p1))
#print(p1.outra)
print(p1.nome)