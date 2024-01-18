listap = []
listai = []

while True:
    n = int(input("Digite um valor : "))
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)

    continuar = str(input("Quer continuar ? [S/N]: ")).strip().upper()

    if continuar in "S":
        print("Continuando...\n")
    elif continuar in "N":
        print("Finalizando o programa...\n")
        break


print(f"A lista completa é {listap + listai}")
print(f"A lista de pares é {listap}")
print(f"A lista de impares é {listai}")