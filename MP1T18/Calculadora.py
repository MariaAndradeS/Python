operacao = input("Escolha sua operação numérica (+, -, *, /, //, %, **): ")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if operacao == "+":
    soma = numero1 + numero2
    print(soma)
elif operacao == "-":
    subtracao = numero1 - numero2
    print(subtracao)
elif operacao == "*":
    multiplicacao = numero1 * numero2
    print(multiplicacao)
elif operacao == "/":
    divisao = numero1 / numero2
    print(divisao)
elif operacao == "//":
    divisaoInteira = numero1 // numero2
    print(divisaoInteira)
elif operacao == "%":
    resto = numero1 % numero2
    print(resto)
elif operacao == "**":
    potencia = numero1 ** numero2
    print(potencia)
else:
    print("Operação inválida")