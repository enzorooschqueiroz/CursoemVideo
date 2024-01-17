num = float(input("Digite um número "
                  "\npara Calcular o seu fatorial : "))

c = num
f = 1
print("Calculando {}!".format(num),end='')
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))