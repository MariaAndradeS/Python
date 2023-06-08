pontuacao1 = int(input())
pontuacao2 = int(input())

if pontuacao1 < 25 and pontuacao2 < 25:
    print("N")
elif pontuacao1 == 25 and pontuacao2 < 24 or pontuacao2 == 25 and pontuacao1 < 24:
    print("S")
elif pontuacao1 - pontuacao2 == 2 or pontuacao2 - pontuacao1 == 2:
    print("S")
else:
    print("N")