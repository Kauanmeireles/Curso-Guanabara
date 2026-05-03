numeros = []
for i in range(2):
    numero = int(input(f'Digite o {i+1} numero: '))
    numeros.append(numero)
    
if numeros[0] == numeros[1]:
    print('\033[1;31mNão existe valor maior os dois sao iguais.\033[m')

else:

 print(f'O Primeiro numero é {max(numeros)} e o Segundo numero é {min(numeros)}')

