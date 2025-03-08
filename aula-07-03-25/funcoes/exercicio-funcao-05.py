# 5. Função de número par ou ímpar
# Crie uma função chamada 'verificar_par' que recebe um número e retorna 'True' se o número for par,
# e 'False' caso contrário. A função pode usar o operador módulo (%) para verificar se o número é divisível por 2.

def verificar_par(a):
    if a % 2 == 0:
        return True
    else:
        return False


num1 = int(input("Informe um numero para saber se é par ou impar: "))
print(verificar_par(num1))
