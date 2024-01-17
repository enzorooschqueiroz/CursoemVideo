num = int(input("Digite um número inteiro : "))
tipo = int(input("\nEscolha uma das bases para conversão\n[1] Transformar para binário \n[2] Transformar para Octal\n[3] Transformar para Hexadecimal\nSua opção : "))

if tipo == 1:
    print("\nO número {} em binário é : {} ".format(num, bin(num)[2:]))
elif tipo == 2:
    print("\nO número {} em Octal é : {} ".format(num, oct(num)[2:]))
elif tipo == 3:
    print("\nO número {} em Hexadecimal é : {} ".format(num, hex(num)[2:]))
else:
    print("\nOpção Inválida, tente novamente.")