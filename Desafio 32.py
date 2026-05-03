from datetime import date
ano = int(input('Me fale o ano e coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano %100 != 0 or ano %400  == 0:
    print(f'Seu ano é de {ano} bisexto!')
else:
    print(f'seu ano de {ano} nao é bisexto.')
