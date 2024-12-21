#genero = "feminino"

genero = input("Olá tud bem? Informe seu Gênero 'Feminino' ou 'Masculino': ").strip().lower()

if genero == "masculino" or genero == "m":
    print ("E ai mano")
elif genero == "feminino" or genero == "f":
    print("E aí miga")
else:
    print("Colé")

print("Código encerrado")
