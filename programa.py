valores_texto = input("Digite os valores separados por espaco: ")

valores = [float(valor) for valor in valores_texto.split()]

if not valores:
    print("Nenhum valor foi informado.")
else:
    soma = sum(valores)
    media = soma / len(valores)

    print(f"Soma: {soma}")
    print(f"Media: {media}")
