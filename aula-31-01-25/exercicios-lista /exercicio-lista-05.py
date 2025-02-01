# 5: Dada a seguinte lista:
# produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
# Crie um algoritmo que ao receber essa lista imprima os itens que iniciam com a letra "a"

produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
letra = 0
resultado = []
palavra = input('Informe qual letra você quer pesquisar para encontrar a palavra: ')
for letra in produtos:
    #print('Retorno da lista: ', letra)
    if letra[0] == palavra:
        resultado.append(letra)

    
print('Lista de palavras que contem a letra ' '"', palavra ,'":', resultado)

# Se não encontrar nenhum item que comece com a letra, resultado será uma lista vazia
if not resultado:
    print(f'Nenhuma palavra encontrada que começa com a letra "{palavra}".')
else:
    print(f'Lista de palavras que começam com a letra "{palavra}":', resultado)
