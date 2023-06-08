memoria = int(input())
memoriaAlocada = 0
maior = 0

while memoria != 0:
    memoriaAlocada = memoriaAlocada + memoria
    memoria = int(input())
    if memoriaAlocada > maior:
        maior = memoriaAlocada
    
print(maior)