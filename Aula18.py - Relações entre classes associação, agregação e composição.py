# Relações entre classes: associação, agregação e composição

# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida indenpendente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de 
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
# HERANÇA / COMPOSIÇÃO

class Carrinho:
    def __init__(self):
        self._produtos = []


    def total(self):
        return sum([p.preco for p in self._produtos])
    

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)


    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Notebook', 1.50), Produto('Mouse', 2.5)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())