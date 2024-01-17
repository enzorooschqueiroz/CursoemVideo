from time import sleep
from random import randint

print("=-="*20)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-="*20)

count = 0
sair = False

while not sair:

    num = int(input("\nDiga um valor [1 a 10] : "))
    choice = str(input("Par ou Ímpar ? [P/I] : ")).strip().upper()
    computador = randint(1, 10)

    print("***" * 20)
    print(f"Você escolheu {num} e o computador escolheu {computador}. Total de {computador + num}")
    print("***" * 20)

    if (computador + num) % 2 == 0 and choice == "P" or (computador + num) % 2 != 0 and choice == "I":
        if choice == "P":
            print("Deu PAR, Você venceu!")
            count += 1

        elif choice == "I":
            print("Deu IMPAR!, Você venceu")
        count += 1
    elif (computador + num) % 2 == 0 and choice == "I" or (computador + num) % 2 != 0 and choice == "P":
        if choice == "P":
            print("Deu IMPAR!, Você PERDEU!")

        elif choice == "I":
            print("Deu PAR!, Você PERDEU")

        print("---" * 20)
        print(f"GAME OVER, você ganhou {count} vezes")
        print("---" * 20)
        break

    else:
        print("!!!" * 20)
        print("Sua escolha de Par ou impar foi inválida, tente novamente...")
        print("!!!" * 20)
        sleep(1)
