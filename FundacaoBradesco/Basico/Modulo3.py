codigo = 10
salario = 1500.00
nome = "Maria"
situacao = True

tipo = type(salario)
print(salario)
print(tipo)
print("Código: " + str(codigo) + " Nome: " + nome)
print("O salario atual é de", salario)

print("---------------------")

codigo1 = 11
salario1 = 1550.560
nome1 = "Cain"
situacao1 = True

print("Codigo: %d" % codigo1)
print("Salario: %.2f" % salario1)
print("Nome: %s" % nome1)
print("Situação: %r" % situacao1)

print("---------------------")

fruta = input()
print(fruta)

numero = int(input())
print("Número Int Long: %ld" % numero)
print("Número Hexadecimal: %x" % numero)
print("Número Octal: %o" % codigo1)

numero1 = float(input())
print("Número Expotencial: %e" % numero1)

print("---------------------")

print("oi\noi")
print("oie\toie")
print("ola\bola")
print("hello\u9177")
