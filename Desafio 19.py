import random
alunos = []
for i in range(4):
    nome = input('Me fale o nome:')
    alunos.append(nome)

sorteado = random.choice(alunos)
print(f'o aluno vai ser é:{sorteado}')