matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
col3 = 0
maior = 0

for l in range (0, 3):
    for c in range (0, 3):
        matriz[l] [c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matriz[l] [c] % 2 == 0:
            pares += matriz[l] [c]
        if c == 2:
            col3 += matriz[l] [c]
        if l == 1:
            maior = matriz[l] [c]
            if matriz[l] [c] > maior:
                maior == matriz[l] [c]




for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end='')
    print()
print(f"A soma dos valores pares foi : {pares}")
print(f"A soma dos valores na terceira coluna foi : {col3}")
print(f"O maior valor da segunda linha é {maior}")

