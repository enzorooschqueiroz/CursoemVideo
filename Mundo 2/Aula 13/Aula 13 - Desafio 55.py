
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input("Digite o Peso da {}° pessoa : ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O menor peso lido foi : {}'.format(menor))
print('O maior peso lido foi : {}'.format(maior))