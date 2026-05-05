soma = 0
for i in range(1, 7):
    num = int(input(f"Digite o {i} numero: "))

    soma += num
print(f"\nA soma total dos numeros é {soma}")

if soma % 2 == 0:

    print("\033[1;32ma soma dos numeros é par\033[m")

else:
    print("\033[1;31ma soma dos numeros é impar desconsidero\033[m")
