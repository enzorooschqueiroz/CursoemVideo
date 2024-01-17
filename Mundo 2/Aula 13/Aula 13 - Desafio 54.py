from datetime import date

counta = 0
countb = 0

for c in range(1, 8):
    ano = int(input("Digite o ano de nascimento do aluno : "))

    if date.today().year - ano >= 18:
        counta += 1
    elif date.today().year - ano < 18:
        countb += 1

print("\nDentro deste grupo {} são maiores de idade, e {} são menores de idade".format(counta, countb))