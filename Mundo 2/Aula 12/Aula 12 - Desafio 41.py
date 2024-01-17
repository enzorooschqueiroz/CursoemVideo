from datetime import date

ano = int(input("Digite o ano de nascimento do atleta : "))
idade = date.today().year - ano

if idade < 9:
    print("O atleta tem {} anos \nA sua categoria é : MIRIM".format(idade))
elif 9 <= idade < 14:
    print("O atleta tem {} anos \nA sua categoria é : INFANTIL".format(idade))
elif 14 <= idade < 19:
    print("O atleta tem {} anos \nA sua categoria é : JÚNIOR".format(idade))
elif 19 <= idade < 25:
    print("O atleta tem {} anos \nA sua categoria é : SÊNIOR".format(idade))
else:
    print("O atleta tem {} anos \nA sua categoria é : MASTER".format(idade))



