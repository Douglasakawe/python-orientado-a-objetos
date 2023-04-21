class Animal:
    #nome = 'Ariranha'

    def init(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, args, **kwargs):
        return self.comendo(args, *kwargs)



    #def acao(self):
        #return(f'{self.nome} está executando uma ação')

Ariranha = Animal(nome='Ariranha')
print(Ariranha.nome)
print(Ariranha.comendo('Peixes'))