from time import sleep

total = menor = caro = cont = 0
produtobarato = " "


while True:
    nome = str(input("\nDigite o nome do produto : "))
    preço = float(input("Digite o preço do produto : "))

    cont += 1
    total += preço
    menor = preço

    if preço > 1000:
        caro += 1
    if cont == 1:
        menor = preço
        produtobarato = nome
    else:
        if preço < menor:
            menor = preço

    continuar = " "
    while continuar not in "S/N":
        continuar = str(input("Deseja adicionar mais produtos? [S/N] : ")).strip().upper()
    if continuar == "N":

        print("\nFinalizando sistema", end="")
        print(".", end='')
        sleep(1)
        print(".", end='')
        sleep(0.75)
        print(".", end='')
        sleep(0.5)
        break


print("\n")
print("---" * 20)
print(f"O total da compra foi : R${total:.2f}")
print(f"O produto mais barato foi : {produtobarato}")
print(f"Você comprou {caro} produtos com o valor maior que 1000 reais")
print("---" * 20)





