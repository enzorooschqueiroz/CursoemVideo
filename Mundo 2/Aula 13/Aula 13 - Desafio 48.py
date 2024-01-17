soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c , end= " ")
        soma += c
        count += 1
print("\nA soma dos {} valores é : {}".format(count, soma))
print("Fim")
