#dados = list()
#pessoas = [["Pedro", 19], ["Enzo", 18], ["Gabriela", 19]]

#dados.append("Pedro")
#dados.append(19)
#pessoas.append(dados[:])
#print(pessoas[1][0])
#print(dados[0])
#print(dados[1])

galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input("\nNome: ")))
    dado.append(int(input("Idade : ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1
print(f"\nTemos {totmai} maiores e {totmen} menores ")