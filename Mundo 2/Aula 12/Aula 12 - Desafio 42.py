r1 = float(input("Digite a medida do primeiro segmento : "))
r2 = float(input("Digite a medida do segmento segmento : "))
r3 = float(input("Digite a medida do terceiro segmento : "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM formar um triangulo")
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo")