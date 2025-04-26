# calculadora.py

# Importando as funções do arquivo calculadora_funcoes.py
from calculadora_funcoes import add, subtract, multiply, divide

def calculator():
    while True:  # Loop que vai continuar até o usuário escolher sair
        print("Calculadora simples")
        print("Escolha a operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        # Solicita a escolha da operação
        choice = input("Digite o número da operação (1/2/3/4/5): ")

        if choice == '5':  # Se o usuário escolher '5', o programa vai parar
            print("Saindo da calculadora. Até logo!")
            break  # Sai do loop e encerra o programa

        # Exibe qual operação o usuário escolheu
        if choice == '1':
            print("Você escolheu a soma...")
        elif choice == '2':
            print("Você escolheu a subtração...")
        elif choice == '3':
            print("Você escolheu a multiplicação...")
        elif choice == '4':
            print("Você escolheu a divisão...")
        else:
            print("Opção inválida")
            continue  # Volta ao início do loop se a opção for inválida

        # Solicita os dois números (somente se a escolha for válida)
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Executa a operação escolhida e exibe o resultado
        if choice == '1':
            print(f"Você escolheu Somar: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Você escolheu Subtrair: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Você escolheu Multiplicar: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Você escolheu Dividir: {num1} / {num2} = {divide(num1, num2)}")

# Inicia a calculadora
calculator()
