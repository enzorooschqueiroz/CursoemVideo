numeros = list()
maior = menor = 0

for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para posição {c} : ")))
    if c == 0:
        maior = numeros[0]
        menor = numeros[0]

    if numeros[c] > maior:
        maior = numeros[c]

    elif numeros[c] < menor:
        menor = numeros[c]

print(f"\nVocê digitou os valores : {numeros}")
print(f"O maior número digitado foi : {maior} nas posições ", end="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i}...", end="")

print(f"\nO menor número digitado foi : {menor} nas posições  : ", end="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i}...", end='')
