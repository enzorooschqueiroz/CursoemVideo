n = s = count = 0

while n != 999:
    n = int(input("Digite um número [999 para parar] : "))
    if n == 999:
        break
    s += n
    count += 1
print(f"A soma desses {count} números vale {s}")
