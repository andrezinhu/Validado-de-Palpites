def changePlayer1():
    print(f"Escolha o nome do time da casa:")
    team1 = input()
    return team1

def changePlayer2():
    print(f"Escolha o nome do time visitante:")
    team2 = input()
    return team2

def changeTeamHome(index):
    print(f"Escolha o nome do time da casa no {index + 1}º confronto:")
    teamHome = input()
    return teamHome

def changeTeamAway(index):
    print(f"Escolha o nome do time visitante no {index + 1}º confronto:")
    teamAway = input()
    return teamAway

def qntGolsHome(index, teamHome):
    print(f"Quantos gols o {teamHome} fez no {index + 1}º jogo? (formato: N)")
    gols = int(input())
    return gols

def qntGolsAway(index, teamAway):
    print(f"Quantos gols o {teamAway} fez no {index + 1}º jogo? (formato: N)")
    gols = int(input())
    return gols

def qntGolsGuessPlayer1TeamHome(index, Player1, teamHome):
    print(f"Quantos gols o {Player1} palpitou que o {teamHome} fez no {index + 1}º jogo? (formato: N)")
    gols = int(input())
    return gols

def qntGolsGuessPlayer1TeamAway(index, Player1, teamAway):
    print(f"Quantos gols o {Player1} palpitou que o {teamAway} fez no {index + 1}º jogo? (formato: N)")
    gols = int(input())
    return gols

def qntGolsGuessPlayer2TeamHome(index, Player2, teamHome):
    print(f"Quantos gols o {Player2} palpitou que o {teamHome} fez no {index + 1}º jogo? (formato: N)")
    gols = int(input())
    return gols

def qntGolsGuessPlayer2TeamAway(index, Player2, teamAway):
    print(f"Quantos gols o {Player2} palpitou que o {teamAway} fez no {index + 1}º jogo? (formato: N)")
    gols = int(input())
    return gols

def compareGuessesAndGols(index, player1, player2, teamHome, teamAway, golsHome, golsAway, guess1Home, guess1Away, guess2Home, guess2Away):
    print(f"Palpite do {player1} no {index + 1}º jogo: {teamHome} {guess1Home} x {guess1Away} {teamAway}")
    print(f"Palpite do {player2} no {index + 1}º jogo: {teamHome} {guess2Home} x {guess2Away} {teamAway}")
    print(f"Placar do {index + 1}º jogo: {teamHome} {golsHome} x {golsAway} {teamAway}")
    print ("----------------------------------")