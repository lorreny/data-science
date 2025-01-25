# Função para calcular a média de um aluno
def calcular_media(notas):
    return sum(notas) / len(notas)

# Solicitar o número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Inicializar variável para calcular a média geral da turma
soma_medias = 0

# Loop para processar as notas de cada aluno
for i in range(num_alunos):
    print(f"\nAluno {i+1}:")
    
    # Solicitar o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Solicitar as 3 notas do aluno
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)
    
    # Calcular a média do aluno
    media = calcular_media(notas)
    
    # Verificar se o aluno foi aprovado ou reprovado
    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    # Exibir o nome, notas, média e situação do aluno
    print(f"\nNome: {nome}")
    print(f"Notas: {notas[0]}, {notas[1]}, {notas[2]}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    
    # Adicionar a média do aluno à soma geral para cálculo da média da turma
    soma_medias += media

# Calcular e exibir a média geral da turma
media_geral = soma_medias / num_alunos
print(f"\nMédia geral da turma: {media_geral:.2f}")
