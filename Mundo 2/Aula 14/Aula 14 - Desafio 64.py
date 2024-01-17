
sair = 999
num = cont = soma = 0
num = float(input("Digite um número [999] para parar : "))
while num != 999:
    cont += 1
    soma += num
    num = float(input("Digite um número [999] para parar : "))

print("{}".format(soma))