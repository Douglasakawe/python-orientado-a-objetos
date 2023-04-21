# Atributos de classe
ANO_ATUAL = 2022

class Pessoa:
    ano_atual = 2022

    def init(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade




p1 = Pessoa('Edmundo', 22)
p2 = Pessoa('Thalita', 12)


print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())