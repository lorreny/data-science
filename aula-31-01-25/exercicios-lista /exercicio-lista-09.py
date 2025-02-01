# 9: Dada duas listas:
# nomes = "Bruna", "Felipe", "Jonathan", "Marcos", "Jéssica"
# sobrenomes = "Silva", "Oliveira", "Rocha", "Marques", "Amaral"
# Crie um algoritmo que imprima o nome completo de cada uma dessas pessoas;
# Essas listas são correspondentes, então a primeira pessoa é "Bruna" e seu sobrenome é "Silva".
# Listas de nomes e sobrenomes
nomes = ["Bruna", "Felipe", "Jonathan", "Marcos", "Jéssica"]
sobrenomes = ["Silva", "Oliveira", "Rocha", "Marques", "Amaral"]

# Percorrendo as duas listas simultaneamente usando zip
for nome, sobrenome in zip(nomes, sobrenomes):
    # Concatenando nome e sobrenome e imprimindo
    print(f"{nome} {sobrenome}")
