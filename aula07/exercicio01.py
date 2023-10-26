class Carro:
    modelo = "Onix"
    marca = "Chevrolet"
    cor = "Cinza"
    ano = 2014
    placa = "JSDA65845A"

    def dadosCarro(self):
        print(f"O modelo é: {self.modelo}, A Marca é: {self.marca}, A Cor é: {self.cor}, O Ano é: {self.ano} e a placa é: {self.placa} ")

carro1 = Carro()

carro1.dadosCarro()

#exercicio02

class Cachorro:
    raça = "Pinscher"
    cor = "preto"
    idade = 9
    nome = "Mickey"
    tutor = "Zé"
    latir = "Au Au"
    comer = "Nham Nham"
    def Cachorro(self,nome):
        self.nome=nome
    
    def skillsCachorro(self):
        print(f"As habilidades são: Latir: {self.latir} e Comer: {self.comer}")

    def dadosCachorro(self):
        print(f"A raça é: {self.raça}, a cor do pelo é: {self.cor}, a idade é: {self.idade}, o nome é: {self.nome} e o tutor é: {self.tutor}")

cachorro1 = Cachorro()
cachorro1.Cachorro("gustavo")
cachorro1.dadosCachorro()
cachorro1.skillsCachorro()
