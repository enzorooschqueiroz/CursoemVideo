temp = []
princ = []
maior = men = 0

while True:
    temp.append(str(input("Nome : ")))
    temp.append(float(input("Peso : ")))
    if len(princ) == 0:
        maior = men = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Deseja continuar ? [S/N] : ")).strip().upper()
    if resp in "N":
        break

print("-=" * 30)
print(f"Ao todo você cadastrou {len(princ)} pessoas")
print(f"O maior peso foi de {maior} KG, Peso de ", end='')
for p in princ:
    if p[1] == maior:
        print(f"{p[0]}", end='')
print()
print(f"O menor peso registrado foi {men}KG. Peso de ", end="")
for p in princ:
    if p[1] == men:
        print(f"{p[0]}", end="")