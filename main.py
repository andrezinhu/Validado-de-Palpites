from utils import math_functions as math_functions
from utils import functions as functions

print ("Olá, esse é o validador de palpite, aqui você ira introduzir os seus palpites de cada jogo, e após isso, irá validar quantos pontos você fez!")
print ("----------------------------------")

player1 = functions.changePlayer1()
player2 = functions.changePlayer2()

print ("Quantos confrontos foram palpitados?")
numeroPalpites = int(input())

teamsHome = []
teamsAway = []

guessesPlayer1Home = []
guessesPlayer1Away = []

guessesPlayer2Home = []
guessesPlayer2Away = []

golsTimesCasa = []
golsTimesFora = []

pontuaçãoTotalCasa = 0
pontuaçãoTotalVisitante = 0

i = 0
while i < numeroPalpites:
    teamsHome.append(functions.changeTeamHome(i))
    teamsAway.append(functions.changeTeamAway(i))

    print(f"Você confirma que o {i + 1}º confronto é entre {teamsHome[i]} e {teamsAway[i]}? 1- Y / 2- N")
    resposta = int(input())

    if resposta == 1:
        print(f"{i + 1}º confronto confirmado!")
        i += 1
    elif resposta == 2:
        teamsHome.pop()
        teamsAway.pop()
        print("Ok, vamos refazer esse confronto.")

i = 0
while i < numeroPalpites:
    golsTimesCasa.append(functions.qntGolsHome(i, teamsHome[i]))
    golsTimesFora.append(functions.qntGolsAway(i, teamsAway[i]))
    print(f"Confirma que o placar do {i + 1}º confronto foi {teamsHome[i]} {golsTimesCasa[i]} x {golsTimesFora[i]} {teamsAway[i]}? 1- Y / 2- N")
    resposta = int(input())
    if resposta == 1:
        print(f"Placar do {i + 1}º confronto confirmado!")
        i += 1
    elif resposta == 2:
        golsTimesCasa.pop()
        golsTimesFora.pop()
        print("Ok, vamos refazer esse placar.")

i = 0
while i < numeroPalpites:
    guessesPlayer1Home.append(functions.qntGolsGuessPlayer1TeamHome(i, player1, teamsHome[i]))
    guessesPlayer1Away.append(functions.qntGolsGuessPlayer1TeamAway(i, player1, teamsAway[i]))
    print(f"Confirma que o palpite do {player1} para o {i + 1}º confronto foi {teamsHome[i]} {guessesPlayer1Home[i]} x {guessesPlayer1Away[i]} {teamsAway[i]}? 1- Y / 2- N")
    resposta = int(input())
    if resposta == 1:
        print(f"Palpite do {player1} para o {i + 1}º confronto confirmado!")
        i += 1 
    elif resposta == 2:
        guessesPlayer1Home.pop()
        guessesPlayer1Away.pop()
        print("Ok, vamos refazer esse palpite.")
print (f"Palpites do {player1} coletados com sucesso!")
print ("----------------------------------")

i = 0
while i < numeroPalpites:
    guessesPlayer2Home.append(functions.qntGolsGuessPlayer2TeamHome(i, player2, teamsHome[i]))
    guessesPlayer2Away.append(functions.qntGolsGuessPlayer2TeamAway(i, player2, teamsAway[i]))
    print(f"Confirma que o palpite do {player2} para o {i + 1}º confronto foi {teamsHome[i]} {guessesPlayer2Home[i]} x {guessesPlayer2Away[i]} {teamsAway[i]}? 1- Y / 2- N")
    resposta = int(input())
    if resposta == 1:
        print(f"Palpite do {player2} para o {i + 1}º confronto confirmado!")
        i += 1 
    elif resposta == 2:
        guessesPlayer2Home.pop()
        guessesPlayer2Away.pop()
        print("Ok, vamos refazer esse palpite.")
print (f"Palpites do {player2} coletados com sucesso!")
print ("----------------------------------")

for i in range (numeroPalpites):
    pontos = math_functions.calculatePointsPlayer1(i, guessesPlayer1Home[i], guessesPlayer1Away[i], golsTimesCasa, golsTimesFora)

    pontuaçãoTotalCasa += pontos
    print (f"Pontuação do {player1} no {i + 1}º jogo: {pontos}")

for i in range (numeroPalpites):
    pontos = math_functions.calculatePointsPlayer2(i, guessesPlayer2Home[i], guessesPlayer2Away[i], golsTimesCasa, golsTimesFora)

    pontuaçãoTotalVisitante += pontos
    print (f"Pontuação do {player2} no {i + 1}º jogo: {pontos}")

print ("----------------------------------")
print (f"Pontuação total do {player1}: {pontuaçãoTotalCasa} pontos!")
print (f"Pontuação total do {player2}: {pontuaçãoTotalVisitante} pontos!")

math_functions.winnerPlayer(player1, player2, pontuaçãoTotalCasa, pontuaçãoTotalVisitante)

print("Gostaria de ver o comparativo dos palpites e dos placares? 1- Y / 2- N")
resposta = int(input())
if resposta == 1:
    for i in range (numeroPalpites):
        functions.compareGuessesAndGols(i, player1, player2, teamsHome[i], teamsAway[i], golsTimesCasa[i], golsTimesFora[i], guessesPlayer1Home[i], guessesPlayer1Away[i], guessesPlayer2Home[i], guessesPlayer2Away[i])
elif resposta == 2:
    print("Ok, obrigado por usar o validador de palpite!")