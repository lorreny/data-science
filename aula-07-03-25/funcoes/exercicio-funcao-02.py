# 2. Função de subtração
# Crie uma função chamada 'subtrair' que recebe dois números e retorna a diferença entre o primeiro e o segundo.
# A função deve retornar a subtração de 'b' de 'a', ou seja, a - b.

def subtracao(a, b):
    result = a - b
    return result

num1 = int(input("Informe o primeiro numero para soma: "))
num2 = int(input("Informe o segundo numero para soma: "))
print(subtracao(num1, num2))
