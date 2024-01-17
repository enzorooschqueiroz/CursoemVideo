frase = str(input("Digite uma frase : ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print("\nVocê digitou a frase : {}".format(junto))

#inverso
for letra in range(len(junto) - 1, -1, -1 ):
    inverso += junto[letra]

print("O inverso de {} é : {}".format(junto, inverso))

#verificação
if inverso == junto:
    print('\nTemos um PALINDROMO')
else:
    print('\nNós NÃO temos um PALINDROMO')