import math
angulo = float(input('Me fale um angulo: '))

rad = math.radians(angulo)

seno = math.sin(rad)
cos  = math.cos(rad)
tan  = math.tan(rad)

print(f'Seno:{seno:.2f}')
print(f'Cosseno: {cos:.2f}')
print(f'Tangente:{tan:.2f}')