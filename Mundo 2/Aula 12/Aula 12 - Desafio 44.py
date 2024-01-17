preço = float(input("Digite o valor do produto : "))
metodo = int(input("\nEscolha a forma de pagamento\n[1] - à vista dinheiro/cheque: 10% de desconto\n[2] - à vista no cartão: 5% de desconto\n[3] - em até 2x no cartão: preço formal \n[4] - 3x ou mais no cartão: 20% de juros\nSua escolha : "))

if metodo == 1:
    desconto = preço - (preço * 0.1)
    print("\nSua compra de ${}, vai custar ${} no final".format(preço, desconto))
elif metodo == 2:
    desconto = preço - (preço * 0.05)
    print("\nSua compra de ${}, vai custar ${} no final".format(preço, desconto))
elif metodo == 3:
    parcelas = 2
    Total = preço / parcelas
    print("\nSua compra vai custar ${}, realizada em {} parcelas de {}".format(preço, parcelas, Total))
elif metodo == 4:
    desconto = preço * 1.20
    parcelas = int(input("Quantas parcelas : "))
    Total = desconto / parcelas
    print("\nSua compra de ${}, vai custar ${} no final, realizado em {} parcelas de ${}".format(preço, desconto, parcelas, Total))
else:
    print("\nOpção inválida, tente novamente")