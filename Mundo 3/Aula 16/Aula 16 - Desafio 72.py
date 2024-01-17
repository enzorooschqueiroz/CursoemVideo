contagem = ("zero", "um", "dois", "três", "quatro", "cinco",
            "seis", "sete", "oito", "nove", "dez",
            "onze", "doze", 'treze', 'catorze', 'quinze',
            'dezesseis', "dezessete", "dezoito", "dezenove", "vinte")

while True:

    escolha = int(input("Escolha um número de 0 a 20 : "))
    if 0 <= escolha <= 20:
        break
    print("Tente novamente")

print(f"Você digitou o número : {contagem[escolha]}")