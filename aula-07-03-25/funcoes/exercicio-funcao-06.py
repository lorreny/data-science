# 6. Função de maior número
# Crie uma função chamada 'maior_numero' que recebe três números e retorna o maior deles.
# A função deve comparar os três valores e retornar o maior deles.
#5 > 3 (Isso é verdadeiro, pois 5 é maior que 3).
#2 > 8 (Isso é falso, pois 2 não é maior que 8).
# Ação se 'a' for maior que 'b'


def maior_numero(a, b, c):
    if a > b and a > c:
        return f'O maior número é {a}'
    elif b > a and b > c:
        return f'O maior número é {b}'
    else:
        return f'O maior número é {c}'
    
input("Vocẽ precisa informar 3 números")
num1 = int(input("Informe o 1° número: "))
num2 = int(input("Informe o 2° número: "))
num3 = int(input("Informe o 3° número: "))
print(maior_numero(num1, num2, num3))
