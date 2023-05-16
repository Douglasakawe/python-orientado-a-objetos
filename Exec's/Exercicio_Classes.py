# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


RS3 = Carro('RS3')
Audi = Fabricante('Audi')
motor_2_0 = Motor('2.0')
RS3.fabricante = Audi
RS3.motor = motor_2_0
print(RS3.nome, RS3.fabricante.nome, RS3.motor.nome)


M3 = Carro('M3')
Bmw = Fabricante('Bmw')
motor_2_0 = Motor('3.0')
M3.fabricante = Bmw
M3.motor = motor_2_0
print(M3.nome, M3.fabricante.nome, M3.motor.nome)


Corolla = Carro('Corolla')
Toyota = Fabricante('Toyota')
Corolla.fabricante = Toyota
Corolla.motor = motor_2_0
print(Corolla.nome, Corolla.fabricante.nome, Corolla.motor.nome)


focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)