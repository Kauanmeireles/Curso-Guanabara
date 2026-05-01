import random
alunos = []

for i in range(4):
    nome = input('Me fale os nomes: ')
    alunos.append(nome)
sorteados = random.choice(alunos)
print(f'O aluno sorteado é {sorteados}!')