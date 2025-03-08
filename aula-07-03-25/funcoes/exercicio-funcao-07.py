# 7. Função de média
# Crie uma função chamada 'calcular_media' que recebe uma lista de números e retorna a média deles.
# A função deve somar todos os números da lista e dividir pelo total de elementos na lista.

def calcular_media(a, b, c):
    soma = a + b + c
    media = soma / 3
    return media

input("Vocẽ precisa informar 3 números para calcularmos a média")
num1 = int(input("Informe o 1° número: "))
num2 = int(input("Informe o 2° número: "))
num3 = int(input("Informe o 3° número: "))
print(calcular_media(num1, num2, num3))

def calcular_media(lista):
    soma = sum(lista)  # soma todos os elementos da lista
    media = soma / len(lista)  # divide pela quantidade de elementos da lista
    return media

# Solicita ao usuário os números
input("Você precisa informar uma lista de números para calcularmos a média")
numeros = [int(input("Informe um número: ")) for _ in range(3)]  # lista de 3 números
print(calcular_media(numeros))
