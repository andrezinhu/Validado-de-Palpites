print ("Olá, esse é o validador de palpite, aqui você ira introduzir os seus palpites de cada jogo, e após isso, irá validar quantos pontos você fez!")

print ("Para começar, quantas partidas são?")
numeroPartidas = int(input())

golsTimesCasa = []
golsTimesFora = []
palpitesCasa = []
palpitesFora = []
pontuaçãoTotal = 0

for i in range (numeroPartidas):
    print (f"Quantos gols o time da casa fez no {i + 1}º jogo? (formato: nXn)")
    numeroGolsCasa = input()
    golsTimesCasa.append(numeroGolsCasa)

    print (f"Quantos gols o time visitante fez no {i + 1}º jogo? (formato: nXn)")
    numeroGolsVisitante = input()
    golsTimesFora.append(numeroGolsVisitante)

for i in range (numeroPartidas):
    print (f"Qual foi o seu palpite para o time da casa no {i + 1}º jogo? (formato: nXn)")
    palpite = input()
    palpitesCasa.append(palpite)

    print (f"Qual foi o seu palpite para o time visitante no {i + 1}º jogo? (formato: nXn)")
    palpite = input()
    palpitesFora.append(palpite)

print ("----------------------------------")
print (f"Palpites dos times de casa: {palpitesCasa}")
print (f"Palpites dos times visitante: {palpitesFora}")

for i in range (numeroPartidas):
    pontos = 0
    if golsTimesCasa[i] == palpitesCasa[i] and golsTimesFora[i] == palpitesFora[i]:
        pontos = 3
    elif (golsTimesCasa[i] == palpitesCasa[i] and golsTimesFora[i] != palpitesFora[i]) or (golsTimesCasa[i] != palpitesCasa[i] and golsTimesFora[i] == palpitesFora[i]):
        pontos = 2
    elif (golsTimesCasa[i] - golsTimesFora[i] == palpitesCasa[i] - palpitesFora[i]):
        pontos = 1
    else:
        pontos = 0
    
    pontuaçãoTotal += pontos
    print (f"Pontuação da partida {i + 1}: {pontos}")

print ("----------------------------------")
print (f"Sua pontuação total foi de: {pontuaçãoTotal} pontos!")