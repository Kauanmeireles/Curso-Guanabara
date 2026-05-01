import math

angulo = float(input('Me fale o grau: '))
hipotenusa = float(input('Digite a Hipotenusa: '))

rad = math.radians(angulo)

co = hipotenusa * math.sin(rad)
ca  = hipotenusa * math.cos(rad)

print(f'Cateto oposto:{co:.2f}')
print(f'Cateto Adjacente:{ca:.2f}')

