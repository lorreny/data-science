#Faça um programa que tenha um número e verifique se o número é positivo, negativo ou neutro
#para saber se um numero é positivo eu posso usar 
numero = int(input("Informe um número: "))

if numero > 0:
    print(f"O número {numero} positivo")
elif numero < 0:
    print(f"O numero {numero} neutro")
else:
    print(f"O número {numero} outro")
