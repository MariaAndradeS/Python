counter = 0
frase = input()

while frase != 'CDA 1942':
    if frase != "":
        counter = counter + 1
    frase = input()
    
print(counter)

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if numero1 > numero2:
    if numero1 > numero3:
        if numero2 < numero3:
            print("maior:", numero1)
            print("menor:", numero2)
        else:
            print("maior:", numero1)
            print("menor:", numero3)
if numero2 > numero1:
    if numero2 > numero3:
        if numero1 < numero3:
            print("maior:", numero2)
            print("menor:", numero1)
        else:
            print("maior:", numero2)
            print("menor:", numero3)
if numero3 > numero1:
    if numero3 > numero2:
        if numero1 < numero2:
            print("maior:", numero3)
            print("menor:", numero1)
        else:
            print("maior:", numero3)
            print("menor:", numero2)


numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

maior = numero1
menor = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3

if numero2 < menor:
    menor = numero2

if numero3 < menor:
    menor = numero3

print("maior:", maior)
print("menor:", menor)