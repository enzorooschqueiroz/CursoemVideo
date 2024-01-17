from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
Computador = randint(0, 2)
print("Vamos Jogar JO-KEN-PÔ?")
jogador = int(input("Faça sua jogada! : \n[0] - PEDRA\n[1] - PAPEL\n[2] - TESOURA\nSua escolha : "))

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!!")
sleep(1)

print("\n")
print("*-" * 15)
print("O Computador escolheu {}".format(itens[Computador]))
print("Você escolheu {}".format(itens[jogador]))
print("*-" * 15)

if Computador == 0:
    if jogador == 0:
        print("\nDEU EMPATE!")
    elif jogador == 1:
        print("\nVOCÊ GANHOU!")
    elif jogador == 2:
        print("\nVOCÊ PERDEU")
    else:
        print("Opção INVÁLIDA")
elif Computador == 1:
    if jogador == 0:
        print("\nVOCÊ PERDEU!")
    elif jogador == 1:
        print("\nDEU EMPATE!")
    elif jogador == 2:
        print("\nVOCÊ GANHOU!")
    else:
        print("Opção INVÁLIDA")
elif Computador == 2:
    if jogador == 0:
        print("\nVOCÊ GANHOU!")
    elif jogador == 1:
        print("\nVOCÊ PERDEU!")
    elif jogador == 2:
        print("\nDEU EMPATE!")
    else:
        print("Opção INVÁLIDA")