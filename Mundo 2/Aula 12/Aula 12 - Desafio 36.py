Casa = float(input("Digite o valor do imóvel : "))
Salario = float(input("Digite o seu salário mensal : "))
Anos = float(input("Em quantos anos pretende pagar? : "))

mensalidade = Casa / (Anos * 12)

print("Para pagar uma casa de ${} em {} anos a prestação será de ${:.2f} por mês".format(Casa, Anos, mensalidade))

if mensalidade >= (Salario * 0.30):
    print("Empréstimo NEGADO")
else:
    print("Empréstimo pode ser APROVADO")