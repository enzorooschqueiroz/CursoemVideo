from random import randint

lista = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print("Os valores sorteados foram : ", end='')

for n in lista:
    print(f"{n} ", end="")

print(f"\n\nO maior valor sorteado foi {max(lista)}")
print(f"O menor valor sorteado foi {min(lista)}")