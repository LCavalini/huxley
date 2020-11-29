n, k = map(int, input().split())
alunos = list()

for i in range(n):
    alunos.append(input().split("-"))

# Ordena pelo segundo elemento (nome do aluno)
alunos.sort(key = lambda item : item[1])

print(f"Matricula: {alunos[k-1][0]}\nNome: {alunos[k-1][1]}")
