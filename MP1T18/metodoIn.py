palavra = input()
sequencia1 = input()
sequencia2 = input()

if palavra in sequencia1 and palavra in sequencia2:
    print(palavra, "CONTIDO EM", sequencia1, "E", palavra, "CONTIDO EM", sequencia2)
elif palavra in sequencia1 and palavra not in sequencia2:
    print(palavra, "CONTIDO EM", sequencia1, "MAS", palavra, "NÃO CONTIDO EM", sequencia2)
elif palavra in sequencia2 and palavra not in sequencia1:
    print(palavra, "NÃO CONTIDO EM", sequencia1, "MAS", palavra, "CONTIDO EM", sequencia2)
else:
    print(palavra, "NÃO CONTIDO EM", sequencia1, "E", palavra, "NÃO CONTIDO EM", sequencia2)