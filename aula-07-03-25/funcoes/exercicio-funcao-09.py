# 9. Função de contar caracteres
# Crie uma função chamada 'contar_caracteres' que recebe uma string e retorna o número de caracteres dessa string.
# A função pode usar a função embutida 'len()' para contar os caracteres da string.

def contar_caracteres(a):
    return f'A palavra "{a}" contém {len(a)} caracteres'

palavra = (input("Informe uma palavra: "))
print(contar_caracteres(palavra))
