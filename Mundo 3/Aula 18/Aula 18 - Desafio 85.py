numeros = [[], []]
num = 1

while True:
    n = int(input(f"\nDigite o {num}° número : "))
    num += 1

    if n % 2 == 0:
        numeros[0].append(n)

    elif n % 2 != 0:
        numeros[1].append(n)

    resposta = str(input("Deseja continuar ? [S/N] :")).strip().upper()

    if resposta in "Nn":
        break

numeros[1].sort()
numeros[0].sort()
print("---" * 15)
print(f"Os números pares digitados foram: {numeros[0]}")
print(f"Os números impares digitados foram : {numeros[1]}")