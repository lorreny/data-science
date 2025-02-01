# 5: Dada a seguinte lista:
# produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
# Crie um algoritmo que ao receber essa lista imprima os itens que iniciam com a letra "a"
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
    print(f'Lista de palavras que começam com a letra "{palavra}":', resultado)
