numero = int(input())
valorInicial = int(input())
valorFinal = int(input())

print("Tabuada do", numero, "de", valorInicial, "até", valorFinal)
for n in range(valorInicial,valorFinal+1):
    resultado = numero * n
    print(numero, "x", n, "=", resultado)