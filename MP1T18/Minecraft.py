
log = int(input("Digite a quantidade de madeira bruta: "))
plank = log * 4
print("A quantidade de madeira é: ", plank)

madeira = int(input("Digite a quantidade de madeira: "))
escada = (madeira // 6) * 4
print("A quantidade de escada é: ", escada)

madeira1 = int(input("Digite a quantidade de madeira: "))
slab = (madeira1 // 3) * 6
print("A quantidade de slab é: ", slab)

print("-------------------------- INVERSO --------------------------")

plank1 = int(input("Digite a quantidade de madeira: "))
log1 = plank1 // 4
print("A quantidade de madeira bruta é: ", log1)

escada1 = int(input("Digite a quantidade de escada: "))
madeira2 = (escada1 * 6) / 4
print("A quantidade de madeira é: ", madeira2)

slab1 = int(input("Digite a quantidade de slab: "))
madeira3 = (slab * 3) / 6
print("A quantidade de madeira é: ", madeira2)
