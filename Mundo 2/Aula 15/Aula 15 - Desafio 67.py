
n = 1

while n != 999:
    print("***"*15)
    num = int(input("Quer ver a tabuada de qual valor ? : "))
    print("***"*15)
    if num < 0:
        break
    elif num >= 0:
        n = 1
        while n <= 10:
            print(f"{num} x {n} = {num*n}")
            n += 1
print("PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE")