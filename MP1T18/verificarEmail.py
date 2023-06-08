quantidade = int(input())
contador = 0
emailErrado = 0
caracter = "gmail"

while contador < quantidade:
    email = input()
    contador += 1
    if caracter not in email:
        emailErrado += 1
        
print(emailErrado)