sex = str(input("Digite seu sexo : [M/F] ")).strip().upper()

while sex not in "MmFf":
    sex = str(input("Valor inválido, por favor indique seu sexo : "))

print("Sexo {} registrado com sucesso!".format(sex))