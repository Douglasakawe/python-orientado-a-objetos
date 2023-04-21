# methods vs @classmethod vs @staticmethod
# method - self, método de instãncia
# @classmethod - cls, método de classe
# @staticmethod - método estático (Xself, Xcls)

# self = inicializa os valores de atributo das instâncias

# Toda vez que for utilziar algo com o 'SELF',
# será um método de instância


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.user = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection




    @staticmethod
    def log(msg):
        print('LOG:', msg)

    def connection_log(msg):
        print('LOG:', msg)


""" c1 = Connection() """

c1 = Connection.create_with_auth('douglas', 'teste1234')

""" c1.set_user('douglas')
c1.set_password('teste123')"""

print(Connection.log('Essa é a mesnsagem de log'))
print(c1.user)
print(c1.password)
