class EmailService:
        
    def enviar(self, msg):
        print('Enviando email: {}'.format(msg))


class Usuario:
    def __init__(self, servicoinjetado):
        self.servicoinjetado = servicoinjetado

    def mandarEmail(self):
        self.servicoinjetado.enviar('olá, tudo bem?')

servico = EmailService()
Usuario = Usuario(servico)
Usuario.mandarEmail()