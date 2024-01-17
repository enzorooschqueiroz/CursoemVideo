#Listas em Python
#As listas podem ser mutáveis, fáceis de ser manipuladas.


num = (2, 5, 6, 9)
valores = [8, 2, 5, 4, 0]
valores.append(10)
valores[2] = 3
valores.sort()
valores.insert(2, 0)
valores.remove(2)
if 5 in valores:
    valores.remove(5)
else:
    print("Não tem 5")

print(valores)
 