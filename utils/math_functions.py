
def calculatePointsPlayer1(index, guessPlayer1Home, guessPlayer1Away, golsHome, golsAway):
    pontos = 0
    if golsHome[index] == guessPlayer1Home and golsAway[index] == guessPlayer1Away:
        pontos = 3
    elif (golsHome[index] == guessPlayer1Home and golsAway[index] != guessPlayer1Away) or (golsHome[index] != guessPlayer1Home and golsAway[index] == guessPlayer1Away):
        pontos = 2
    elif (golsHome[index] - golsAway[index] == guessPlayer1Home - guessPlayer1Away):
        pontos = 1
    else:
        pontos = 0
    return pontos

def calculatePointsPlayer2(index, guessPlayer2Home, guessPlayer2Away, golsHome, golsAway):
    pontos = 0
    if golsHome[index] == guessPlayer2Home and golsAway[index] == guessPlayer2Away:
        pontos = 3
    elif (golsHome[index] == guessPlayer2Home and golsAway[index] != guessPlayer2Away) or (golsHome[index] != guessPlayer2Home and golsAway[index] == guessPlayer2Away):
        pontos = 2
    elif (golsHome[index] - golsAway[index] == guessPlayer2Home - guessPlayer2Away):
        pontos = 1
    else:
        pontos = 0
    return pontos

def winnerPlayer(player1, player2, scorePlayer1, scorePlayer2):
    if scorePlayer1 > scorePlayer2:
        print (f"O {player1} venceu a rodada!")
    elif scorePlayer2 > scorePlayer1:
        print (f"O {player2} venceu a rodada!")
    elif scorePlayer1 == scorePlayer2:
        print (f"Empate! Ambos os jogadores tiveram o mesmo número de pontos nessa rodada!")
    else:
        print (f"Erro na contagem de pontos. Verifique os cálculos.")