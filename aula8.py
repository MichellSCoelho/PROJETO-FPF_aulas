#import datetime as dt

#entradaNome = input('digite seu nome: ')

#print(f'Seu nome é {entradaNome}, e agora é: {dt.datetime.now().time()}')


umaVariavel = 10
print(f"{umaVariavel} é {type(umaVariavel)}")

umaVariavel = "hellor world"
print(f'{umaVariavel} é {type(umaVariavel)}')

umaVariavel = 10.5
print(f'{umaVariavel} é {type(umaVariavel)}')

umaVariavel = True
print(f'{umaVariavel} é {type(umaVariavel)}')

umaVariavel = None
print(f'{umaVariavel} é {type(umaVariavel)}')


#type Hint ( dica do dia)

varialvelNumero: int = 10
varialvelFloat: float = 3.14
variavelString: str = "hello world"
variavelBoolean: bool = False

#INPUT

exemploInput1 = int(input("digite um numero:"))
exemploInput2 = int(input("digite outro numero:"))

print(f' A soma é: {exemploInput1 + exemploInput2}')
