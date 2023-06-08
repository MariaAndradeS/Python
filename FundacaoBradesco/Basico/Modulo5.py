def mensagem1(): #função
    print("Olá Mundo")
    
def mensagem2():
    return 'Hello World'

mensagem1()
texto = mensagem2()
print(texto)
    
print("------------------------")

def lernotas():
    nota=float(input('Digite uma nota para o aluno: '))
    return nota

def resultado(nota1, nota2):
    media=(nota1 + nota2)/2
    print("Nota 1: ", nota1)
    print("Nota 2: ", nota2)
    print("Media:", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else: 
        print("Reprovado")
        
n1 = lernotas()
n2 = lernotas()
resultado(n1, n2)