print("*-" * 15)
print("       TERMOS DE UMA PA")
print("*-" * 15)

termo = int(input("\nPrimeiro termo : "))
razao = int(input("Razão : "))
decimo = termo + (10 - 1) * razao

for c in range (termo, decimo + razao, razao):
    print(c, end=" ->")

print("ACABOU")