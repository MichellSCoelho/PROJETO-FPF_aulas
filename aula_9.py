#funções com argumentos nomeados Vs. argumentos posicionais

#função com argumento posicionais
#TODA a função em python começa com um 'def'
def somarPosicional(num1, num2):
    print(f' o numero 1 tem valor: {num1}')
    print(f' o numero 2 tem valor: {num2}')
    return num1 + num2

#print(somarPosicional(4, 8))

#FUNÇÃO COM ARGUMENTO NOMEADOS ex.: num2= 8 , onde a posição do argumento é nomeado
#1 usage
#como a gente faz pra colocar VALOR PADRÃO NUM ARGUMENTO? No def(exponencialNomeado) coloca-se o valor 1 ou zero
# o caracter \n é uma nova linha
def exponencialNomeado(num1=1, num2=1):
    print(f' o numero 1 tem valor: {num1}')
    print(f' o numero 2 tem valor: {num2}')
    return num1 ** num2

#print(exponencialNomeado(num2=8, num1=4))
print(exponencialNomeado(num1=5))

#PRINT() com argumentos extras
num1 = 10
num2 =20
print(num1, num2, sep= ' - ', end= '\n')

# F STRING
print(f'num1 é {num1} | num2 é {num2}')

# o .format é uma forma de achar o valor e posicionar dentro na string posicional
print('num1 é {} | num2 é {}' .format(num1, num2))
#forma posicional
print('num1 é {n1} | num2 é {n2}' .format(n1=num1, n2=num2)) 

#adição em Python
print(f'Adição: {num1 + num2}')
print(f'Subtração: {num1 - num2}')
print(f'Multiplicação: {num1 * num2}')
print(f'Divisão: {num1 / num2}') #resultado 2.0 (float) sendo a divisão com 1 barra /
print(f'Divisão: {num1 // num2}') #resultado 2 , divisão inteira
print(f'Módulo: {num1 % num2}') #resto da divisão, ou porcentagem
print(f'Exponencial: {num1 ** num2}') 


#OPERAÇÕES RELACIONAIS
print(f'Maior que: {num1 > num2}') #Maiorque > , resposta=False
print(f'Maior igual a: {num1 >= num2}') #maoir igual é icnluido um num, resposta=false  
print(f'Menor que: {num1 < num2}') #resposta=TRue
print(f'Menor igual a: {num1 <= num2}') # RES. TRUE
print(f'É igual a: {num1 == num2}')
print(f'É diferente: {num1 != num2}')

#OPERADORES LOGICOS
num3 = 15
print(f'usado and a: {num1 < num2 and num2 > num1}')
print(f'usado or: {num1 > num2 or num2 > num1}')
print(f'usado not: {not num1 > num2 }')

