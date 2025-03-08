# 3. Função de multiplicação
# Crie uma função chamada 'multiplicar' que recebe dois números e retorna o produto deles.
# A função deve retornar o valor da multiplicação entre os dois números passados como parâmetros.

def multiplicar(a, b):
    result = a * b
    return result

num1 = int(input("Informe o primeiro numero para multiplicar: "))
num2 = int(input("Informe o segundo numero para multiplicar: "))
print(multiplicar(num1, num2))
