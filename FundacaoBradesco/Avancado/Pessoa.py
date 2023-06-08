class Pessoa:
    "Isto é uma pesssoa chamada Maria"
    idade = 16
    
    def saudacao(self): #self -> o primeiro argumento da função na classe deve ser o próprio objeto
        print("Olá Maria!")
        
print(Pessoa.idade)
print(Pessoa.__doc__)

Cain = Pessoa()
print(Cain.idade)
Cain.saudacao() #mesma coisa que -> Pessoa.saudacao(Cain)