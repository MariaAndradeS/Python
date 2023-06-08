questoes = ['No'] * 4
respostas = input()

while respostas != "timeout":
    for i in range (1,5):
        if respostas == ('accepted' + str(i)):
            questoes[i-1] == 'Yes'
    respostas = input()
        
print(*questoes)