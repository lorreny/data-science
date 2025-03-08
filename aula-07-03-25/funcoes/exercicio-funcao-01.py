# 1. Função de soma
# Crie uma função chamada 'soma' que recebe dois números como parâmetros e retorna a soma deles.
# A função deve aceitar dois números e retornar o resultado da soma entre eles.

def soma(a, b):
    result = a + b
    return result

num1 = int(input("Informe o primeiro numero para soma: "))
num2 = int(input("Informe o segundo numero para soma: "))
print(soma(num1, num2))
