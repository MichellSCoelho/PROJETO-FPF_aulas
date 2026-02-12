class Mensagem:
    def enviar (self, texto):
        print(f'Mensagem enviada: {texto}')

class Usuario:
    def __init__(self, msg):
        self.msg = msg

    def notificar (self, texto):
        self.msg.enviar(texto)

m = Mensagem()
u = Usuario(m)
u.notificar("Bem-vindo")

class Veiculo:
    def mover(self):
        pass

class Motor:
    def ligar (self):
        print("motor ligado")

class Carro (Veiculo):
    def __init__(self, motor):
        self.motor = motor
    def mover(self):
        self.motor.ligar()
        print(f'motor ligado')

m = Motor()
c = Carro(m)
c.mover()