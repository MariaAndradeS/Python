saldo = float(input())
compras = float(input())
contador = 0

while (saldo - compras) >= 0:
    saldo = saldo - compras
    contador = contador + 1
    compras = float(input())
    
print("Número de itens", contador)
print("Saldo: %.2f" % saldo)