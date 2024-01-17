
somaidade = 0
mediaidade = 0
nomevelho = " "
maioridade = 0
totmulher20 = 0

for c in range (1, 5):
    print("-----{}° PESSOA -----".format(c))
    nome = str(input("Digite seu nome : "))
    idade = int(input("Digite sua idade : "))
    sexo = str(input("Digite seu sexo [M/F] : "))
    somaidade += idade

    if c == 1 and sexo in "Mm":
        maioridade = idade
        nomevelho = nome

    if sexo in "Mm" and idade > maioridade:
        maioridade = idade
        nomevelho = nome

    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print("\n")
print("*-*" * 18)
print("A média da idade das pessoas no grupo é: {} ".format(mediaidade))
print("O Homem mais velho tem {} anos e seu nome é {}".format(maioridade, nomevelho))
print("O total de mulheres abaixo de 20 anos é : {}".format(totmulher20))
print("*-*" * 18)
