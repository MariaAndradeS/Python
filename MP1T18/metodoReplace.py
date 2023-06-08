cpf = input()
caracter1 = "-"
caracter2 = "."

if caracter1 in cpf and caracter2 in cpf:
    cpf = cpf.replace(caracter1, "")
    cpf = cpf.replace(caracter2, "")
    print(cpf)
elif caracter1 in cpf and caracter2 not in cpf:
    cpf = cpf.replace(caracter1, "")
    print(cpf)
elif caracter1 not in cpf and caracter2 in cpf:
    cpf = cpf.replace(caracter2, "")
    print(cpf)
else:
    print(cpf)
    
if len(cpf) == 11:
    print("OK")
else:
    print("ERROR")