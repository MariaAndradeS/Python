dados = input()
caracter = input()

for c in caracter:
    dados = dados.replace(c, "*")
    
print(dados)