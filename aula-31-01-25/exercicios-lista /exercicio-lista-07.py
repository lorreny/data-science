# 7: Crie um algoritmo que ao receber uma lista imprima todos os itens que contenham uma letra determinada por você.

produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]

resultado = []
palavra = input('Informe qual letra você quer pesquisar para encontrar a palavra: ')

# Percorrer todos os itens da lista 'produtos'
for letra in produtos:
    # Verificar se a primeira letra da palavra corresponde à letra informada
    if palavra in letra:  #aqui não pesquisa pelo indice
        resultado.append(letra)

# Se não encontrar nenhum item que comece com a letra, resultado será uma lista vazia
if not resultado:
    print(f'Nenhuma palavra encontrada que começa com a letra "{palavra}".')
else:
    print(f'Lista de palavras que contenha a letra "{palavra}":', resultado)

