peso = float(input("Digite o seu peso (ex 78) : "))
altura = float(input("Digite a sua altura (ex. 1.88 : "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("\nSeu IMC é : {}\nVocê está Abaixo do peso!".format(imc))
elif 18.5 <= imc < 25:
    print("\nSeu IMC é : {}\nVocê está no Peso ideal".format(imc))
elif 25<= imc < 30:
    print("\nSeu IMC é : {}\nVocê está Sobrepeso!".format(imc))
elif 30 <= imc < 40:
    print("\nSeu IMC é : {}\nVocê está Obeso".format(imc))
else:
    print("\nSeu IMC é : {}\nVocê está EM Obesidade Morbida".format(imc))