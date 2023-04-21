# @Property + @Setter - getter e setter no modo Pythônico

# - como getter
# - p/  evitar quebra de código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começam com um ou dois underline (_)
# Não devem ser usados fora da classe.


class Caneta:
    def __init__(self, cor):
        # private, protected
        self._cor = cor
        self.cor_tampa = None


    @property
    def cor(self):
        print('Estou no Getter')
        return self._cor
    

    @cor.setter 
    def cor(self, valor):
        print('Estou no Setter')
        self._cor = valor


    @property
    def cor_tampa(self):
        return self._cor_tampa
    

    @cor_tampa.setter
    def cor_tampa(self, valor ):
        self._cor_tampa = valor



caneta = Caneta('Azul')
caneta._cor = 'Blue'
caneta.cor_tampa = 'Green'
print(caneta.cor)
print(caneta.cor_tampa)

# getter ---> obter valor
