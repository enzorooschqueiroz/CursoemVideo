from datetime import date

Hoje = date.today().year
aniversário = int(input("Digite o ano do seu nascimento : "))

idade = Hoje - aniversário

if idade > 18 :
    Alistamento = Hoje - (idade - 18)
    print("\nQuem nasceu em {} tem {} anos em {}\nVocê deveria ter se apresentado há {} anos\nSeu ano de Alistamento foi em {}".format(aniversário, idade, Hoje, (idade - 18), Alistamento))

elif idade < 18:
    Alistamento = (18 - idade) + Hoje
    print("\nQuem nasceu em {} tem {} anos em {}\nVocê vai se apresentar em {} anos\nSeu ano de Alistamento será em {}".format(aniversário, idade, Hoje, (18 - idade), Alistamento))

else:
    print("\nQuem nasceu em {} tem 18 anos em {}\n ****SE APRESENTE IMEDIATAMENTE****".format(aniversário, Hoje))