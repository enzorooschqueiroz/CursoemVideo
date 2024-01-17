nome = str(input("Digite o nome do aluno : "))
nota1 = float(input("\nDigite a primeira nota do aluno : "))
nota2 = float(input("Digite a segunda nota do aluno : "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("A média do aluno foi : {}\n****APROVADO****".format(nome, media))
elif media < 5:
    print("A média do aluno {} foi : {}\n****REPROVADO****".format(nome, media))
elif 7 > media >= 5:
    print("A média do aluno {} foi : {}\n****RECUPERAÇÃO****".format(nome, media))