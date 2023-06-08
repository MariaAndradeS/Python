algarismo = input()

for num in algarismo:
    contador = int(num)
    histograma = ""
    
    if contador != 0:
        for _ in range(contador):
            histograma += "*"
        print(histograma)