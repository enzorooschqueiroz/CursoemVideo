from time import sleep

print("Escolha dois números:")
num1 = float(input("Primeiro número : "))
num2 = float(input("Segundo número : "))

sair = False

while not sair:
    escolha = int(input("\nEscolha operação quer fazer com estes números: "
                        "\n[1] - Soma"
                        "\n[2] - Multiplicação"
                        "\n[3] - Descobrir qual é o maior"
                        "\n[4] - Escolher novos números"
                        "\n[5] - Sair"
                        "\nSua escolha : "))

    if escolha == 1:
        result = num1 + num2
        print("A soma dos números {} e {} é igual a : {} ".format(num1, num2, result))
        continuar = str(input("Deseja continuar? [S/N] : "))
        if continuar == "S":
            print("Ok")
        else:
            print("\nDesligando")
            print("3...")
            sleep(0.5)
            print("2..")
            sleep(0.5)
            print("1.")
            sleep(0.5)
            sair = True

    elif escolha == 2:
        result = num1 * num2
        print("{} vezes {} é igual a : {} ". format(num1, num2, result))
        continuar = str(input("Deseja continuar? [S/N] : "))
        if continuar == "S":
            print("Ok")
        else:
            print("\nDesligando")
            print("3...")
            sleep(0.5)
            print("2..")
            sleep(0.5)
            print("1.")
            sleep(0.5)
            sair = True

    elif escolha == 3:
        if num1 > num2:
            print("O primeiro número é maior")
            continuar = str(input("Deseja continuar? [S/N] : "))
            if continuar == "S":
                print("Ok")
            else:
                print("\nDesligando")
                print("3...")
                sleep(0.5)
                print("2..")
                sleep(0.5)
                print("1.")
                sleep(0.5)
                sair = True
        elif num1 < num2:
            print("O segundo número é maior")
            continuar = str(input("Deseja continuar? [S/N] : "))
            if continuar == "S":
                print("Ok")
            else:
                print("\nDesligando")
                print("3...")
                sleep(0.5)
                print("2..")
                sleep(0.5)
                print("1.")
                sleep(0.5)
                sair = True
        else:
            print("Eles são iguais")
            continuar = str(input("Deseja continuar? [S/N] : "))
            if continuar == "S":
                print("Ok")
            else:
                print("\nDesligando")
                print("3...")
                sleep(0.5)
                print("2..")
                sleep(0.5)
                print("1.")
                sleep(0.5)
                sair = True

    elif escolha == 4:
        num1 = float(input("Novo primeiro número : "))
        num2 = float(input("Novo segundo número : "))

    elif escolha == 5:
        print("\nDesligando")
        print("3...")
        sleep(0.5)
        print("2..")
        sleep(0.5)
        print("1.")
        sleep(0.5)
        sair = True