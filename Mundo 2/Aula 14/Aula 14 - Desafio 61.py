termo = int(input("Digite o termo da PA : "))
razão = int(input("Digite a razão da PA : "))

c = 0
while c != 10:
    print("{}".format(termo), end="->")
    termo += razão
    c += 1
print("FIM")