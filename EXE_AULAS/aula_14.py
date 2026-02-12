class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def cumprimentar(self):
        print(f'Olá sou {self.nome}, e tenho {self.idade} anos')


class Carro:
    def __init__(self, marca: str, modelo: str, cor: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def ligar_motor(self):
        print(f'Ligando motor de { self.marca}')

    def desligar_motor(self):
        print(f'Desligar motor de {self.marca}')

meuCarro = Carro('BYD', 'Dolphin', 'Rosa', 2026)
meuCarro.ligar_motor()





