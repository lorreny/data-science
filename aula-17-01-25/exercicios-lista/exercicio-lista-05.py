produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
letra = 0
resultado = []
palavra = input('Informe qual letra você quer pesquisar para encontrar a palavra: ')
for letra in produtos:
    #print('Retorno da lista: ', letra)
    if letra[0] == palavra:
        resultado.append(letra)
    
print('Lista de palavras que contem a letra ' '"', palavra ,'":', resultado)
