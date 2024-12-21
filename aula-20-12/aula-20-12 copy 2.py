#Faça um programa que recebe uma idade e verifique se a pessoa pode votar no brasil
#menor de 16 não vota
#entre 16 e 18 ou acima de 70 o voto é facultativo
#entre 18 e 70 o voto é obrigatório

#>	Maior que	Verdadeiro se o valor à esquerda exceder o valor à direita
#<	Menor que	Verdadeiro se o valor à esquerda for menor que o valor à direita

idade = int(input("Informe a sua idade: "))

if idade <= 16:
    print(f"Você não pode votar {idade}")
elif (idade >= 16 and idade < 18) or idade > 70:
    print(f"Seu voto é opcional {idade}")
else:
    print(f"Parabéns você pode votar")

#### outra opção

idade = int(input("Informe a sua idade: "))

if idade <= 16:
    print(f"Você não pode votar {idade}")
elif idade < 18: 
    print(f"Seu voto é opcional {idade}")
elif idade < 70:
    print(f"Seu voto é opcional {idade}")
else:
    print(f"Parabéns você pode votar")
