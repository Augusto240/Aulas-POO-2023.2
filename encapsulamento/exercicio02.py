class Cliente:
    def __init__(self, nome=str, cpf=str, renda=float):
        self.__nome = nome
        self.__cpf = cpf
        self.__renda = renda
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter 
    def setNome(self, nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def setCPF(self, cpf):
        self.__cpf = cpf
    
    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def setRenda(self, renda):
        self.__renda = renda

p1 = Cliente("Zézinho", "022.017.777-22", 5000.00)
print(f'Meu nome é: {p1.nome}')
print(f'Meu CPF é: {p1.cpf}')
print(f'Minha renda é de: R$ {p1.renda}')