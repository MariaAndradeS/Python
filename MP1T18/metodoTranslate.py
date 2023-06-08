cpf = input()
caracter = '.-'

cpfLimpo = cpf.translate(str.maketrans('','', caracter))
verificacao = cpfLimpo.isdigit()

if  len(cpfLimpo) == 11 and verificacao == False:
    print("ENCODING ERROR")
elif len(cpfLimpo) != 11 and verificacao == True:
    print("SIZE ERROR")
elif len(cpfLimpo) != 11 and verificacao == False:
    print("ENCODING ERROR")
    print("SIZE ERROR")
else:
    print(cpfLimpo)