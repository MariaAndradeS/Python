pontuacao1 = 0
pontuacao2 = 0
condicao = ""

while condicao != "S":
    pontuacaoGeral = int(input())
    if pontuacaoGeral == 1:
        pontuacao1 = pontuacao1 + 1
    elif pontuacaoGeral == 2:
        pontuacao2 = pontuacao2 + 1
    if pontuacao1 < 25 and pontuacao2 < 25:
        condicao = "N"
    elif pontuacao1 == 25 and pontuacao2 < 24 or pontuacao2 == 25 and pontuacao1 < 24:
        condicao = "S"
    elif pontuacao1 - pontuacao2 == 2 or pontuacao2 - pontuacao1 == 2:
        condicao = "S"
    else:
        condicao = "N"

print(pontuacao1, "x", pontuacao2)