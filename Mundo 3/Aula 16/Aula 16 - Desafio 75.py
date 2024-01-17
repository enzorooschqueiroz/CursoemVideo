
num = (int(input("Digite um número : ")),
        int(input("Digite mais um número : ")),
        int(input("Digite outro número : ")),
        int(input("Digite só mais um númerozinho : ")))

print(f"\nVocê digitou os valores {num}")

print(f"O número 9 apareceu {num.count(9)} vezes")

if 3 in num:
    print(f"O primeiro número três digitado está na posição {num.index(3)+1}")
else:
    print("O valor 3 não foi digitado")

print(f"Os números pares digitados foram  : ", end="")

for n in num:
    if n % 2 == 0:
        print(n, end="  ")
       