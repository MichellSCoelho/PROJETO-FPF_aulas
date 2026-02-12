class EmailService:
    def enviar(self, msg):
        print('Enviando email: {}'.format(msg))


class Usuario:
    def __init__(self, servicoinjetado):
        self.servicoinjetado = servicoinjetado

    def mandarEmail(self):
        self.servicoinjetado.enviar("Olá, tudo bem?")


usuario = Usuario(EmailService())
usuario.mandarEmail()