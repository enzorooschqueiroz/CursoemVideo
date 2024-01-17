from time import sleep

mulher20 = homens = adultos = 0
while True:
    print("---"*15)
    print("CADASTRE UMA PESSOA")
    print("---"*15)


    idade = int(input(("Digite sua idade : ")))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F] : ")).strip().upper()

    if idade >= 18:
        adultos += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulher20 += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N] : ")).strip().upper()
    if continuar == "N":
        print("Finalizando sistema", end="")
        print(".", end='')
        sleep(1)
        print(".", end='')
        sleep(0.75)
        print(".", end='')
        sleep(0.5)
        break

print("\n")
print("+++"*20)
print(f"Total de pessoas adultas : {adultos}")
print(f"Total de Homens cadastrados : {homens}")
print(f"Total de mulheres com menos que 20 anos : {mulher20}")
print("+++"*20)
