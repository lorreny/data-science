# 4. Função de divisão
# Crie uma função chamada 'dividir' que recebe dois números e retorna o quociente da divisão.
# A função deve realizar a divisão de 'a' por 'b', mas é importante verificar se o divisor 'b' é zero.
# Se for zero, a função deve retornar uma mensagem de erro ou um valor indicativo (ex: "Erro: Divisão por zero").

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    else:
        result = a / b
        return result

num1 = int(input("Informe o primeiro numero para dividir: "))
num2 = int(input("Informe o segundo numero para dividir: "))
print(dividir(num1, num2))
