from random import randint

computador = randint(0, 10)
print("Sou seu computador, escolhi um número de 0 a 10, você consegue descobrir?")
acertou = False
palpite = 0
chances = 5

while not acertou:
    jogador = int(input("Digite seu palpite : "))
    if jogador == computador:
        palpite += 1
        acertou  = True
    else:
        if jogador > computador:
            print("Menos!!!, tente de novo.")
            palpite += 1
        elif jogador < computador:
            print("Mais!!!, tente de novo.")
            palpite += 1

print("Você acertou!!!, em {} tentativas".format(palpite))











#numeros = (0, 10)
#computador = randint(0, 10)
#guess = int(input("Digite um número de 1 a 10 : "))

#while guess != computador:
    #guess = int(input("Errou, tente novamente : "))

#print("Acertou!")