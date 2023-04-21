# Hard coded - É algo que foi escrito diretamente no código
# Métodos em instâncias de classes python

class Carro:
    def init(self, nome):
        self.nome = nome


    def acelerar(self):
        print(f'{self.nome} está acelerando...')

audi = Carro('audi')
print(audi.nome)
audi.acelerar()

bmw = Carro('bmw')
print(bmw.nome)
bmw.acelerar()