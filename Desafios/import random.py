import random

print(""" Escolha uma Das opções
[1] Pedra
[2] Papel
[3] Tesoura
      """)
opcao = int(input("Coloque a opção: "))
maquina = random.randint(1, 3)
if opcao == 1 and maquina == 3:
    print("Voce ganhou, pedra ganha de tesoura!")
elif opcao == maquina:
    print("empate!")
elif opcao == 2 and maquina == 1:
    print("Voce ganhou! Papel ganha de pedra!")
elif opcao == 3 and maquina == 2:
    print("Voce ganhou! Tesoura ganha de Papel")
elif maquina == 1 and opcao == 3:
    print("Voce perdeu,Tesoura perde pra pedra...")
elif maquina == 2 and opcao == 1:
    print("Voce perdeu, Pedra perde para papel...")
elif maquina == 3 and opcao == 2:
    print("Voce perdeu, Papel perde para Tesoura...")
else:
    print("opção errada")
