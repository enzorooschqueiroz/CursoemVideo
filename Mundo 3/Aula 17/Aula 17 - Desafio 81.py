lista = []
count = c = 0

while True:
    n = int(input("Digite um número : "))
    count += 1
    if c == 0 or n < lista[-1]:
        lista.append(n)
        c +=1
    else:
        pos = 0
        while pos < len(lista):
            if n >= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

    sair = str(input("Deseja continuar? [S/N] : ")).strip().upper()

    if sair in "S":
        print("Continuando...\n")
    elif sair in "N":
        print("Finalizando o Programa ...\n")
        break

print(f"Você digitou {count} números")
print(f"A lista em ordem decrescente é {lista}")
if 5 in lista:
    print("Você digitou o número 5 !")
else:
    print("Você NÃO digitou o número 5 !")