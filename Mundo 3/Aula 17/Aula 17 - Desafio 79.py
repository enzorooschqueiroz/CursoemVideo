numeros = list()
print("Lista de números únicos : ")
while True:
    n = int(input("\nDigite um valor : "))
    if n not in numeros:
        numeros.append(n)
        print("Número adicionado com sucesso!")
    else:
        print("Valor duplicado! não foi adicionado")

    sair = str(input("Deseja continuar ? [S/N] : ")).strip().upper()

    if sair in "N":
        break

numeros.sort()
print(f"\nOs valores digitados foram {numeros}")