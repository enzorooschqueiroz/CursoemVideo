primeiro = int(input("Digite o termo da PA : "))
razão = int(input("Digite a razão da PA : "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}".format(termo), end="->")
        termo += razão
        cont +=1
    print("PAUSA")
    mais = int(input("Quantos termos quer adicionar? : "))
print("Progressão finalizada")

