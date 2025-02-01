# 8: Crie um algoritmo que ao receber uma lista númerica, imprima a multiplicação de cada um dos elementos da lista por 2.add()


multiplicar = [2, 3, 6, 8]
resultado = []
for numero in multiplicar:
    resultado.append(numero*2)

print(resultado) #aqui imprime os valores da lista


numeros = (input('Informe 1 ou mais números para fazermos a multiplicação, sem pontuação apenas com espaço: '))

converter = numeros.split()

converter = list(map(int, converter))
print(converter) #aqui imprime os valores da lista

resultado = []
for numero in converter:
    resultado.append(numero*2)

print(resultado) #aqui imprime os valores da lista
