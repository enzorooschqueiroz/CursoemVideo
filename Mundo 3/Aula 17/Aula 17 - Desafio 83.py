expressão = str(input("Digite uma expressão : "))
pilha = []

for simb in expressão:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("\nSua expressão está válida ! ")
else:
    print("\nSua expressão está inválida ! ")