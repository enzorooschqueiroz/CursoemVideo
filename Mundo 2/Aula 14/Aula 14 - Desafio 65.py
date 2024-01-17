media = 0
soma = 0
count = 0
maior = 0
menor = 0
sair = False

num = float(input("Digite um número : "))
maior = num
menor = num
while not sair:
    count += 1
    soma += num
    verificacao = str(input("Deseja continuar? [S/N] : ")).strip().upper()
    if verificacao == "N":
        sair = True
    elif verificacao == "S":
        num = float(input("Digite um número : "))
    else:
        print("Opção INVÁLIDA, tente novamnete")

    if num >= maior:
        maior = num

    elif num <= menor:
        menor = num

media = soma / count

print("\n")
print("---"*20)
print("Você digitou {} valores, e a a media entre eles é:  {}".format(count, media))
print("O menor número digitado foi : {}"
      "\nO maior número digitado foi : {}".format(menor, maior))
print("---"*20)




