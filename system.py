print ("Olá, esse é o validador de palpite, aqui você ira introduzir os seus palpites de cada jogo, e após isso, irá validar quantos pontos você fez!")
print ("----------------------------------")

print("Como se chama o time da casa?")
timeCasa = input()
print("Como se chama o time visitante?")
timeVisitante = input()

print ("Para começar, quantos jogos palpitados são?")
numeroPalpites = int(input())

palpitesTimeCasa1 = []
palpitesTimeCasa2 = []

palpitesTimeVisitante1 = []
palpitesTimeVisitante2 = []

golsTimesCasa = []
golsTimesFora = []
palpitesCasa = []
palpitesFora = []

pontuaçãoTotalCasa = 0
pontuaçãoTotalVisitante = 0

for i in range (numeroPalpites):
    print (f"Quantos gols o time da casa fez no {i + 1}º jogo? (formato: N)")
    numeroGolsCasa = int(input())
    golsTimesCasa.append(numeroGolsCasa)

    print (f"Quantos gols o time visitante fez no {i + 1}º jogo? (formato: N)")
    numeroGolsVisitante = int(input())
    golsTimesFora.append(numeroGolsVisitante)

for i in range (numeroPalpites):
    print (f"Qual foi o palpite do {timeCasa} para o time da casa no {i + 1}º jogo? (formato: N)")
    palpite = int(input())
    palpitesTimeCasa1.append(palpite)

    print (f"Qual foi o palpite do {timeCasa} para o time visitante no {i + 1}º jogo? (formato: N)")
    palpite = int(input())
    palpitesTimeCasa2.append(palpite)
print (f"Palpites do {timeCasa} coletados com sucesso!")
print ("----------------------------------")

for i in range (numeroPalpites):
    print (f"Qual foi o palpite do {timeVisitante} para o time da casa no {i + 1}º jogo? (formato: N)")
    palpite = int(input())
    palpitesTimeVisitante1.append(palpite)

    print (f"Qual foi o palpite do {timeVisitante} para o time visitante no {i + 1}º jogo? (formato: N)")
    palpite = int(input())
    palpitesTimeVisitante2.append(palpite)
print (f"Palpites do {timeVisitante} coletados com sucesso!")
print ("----------------------------------")

print (f"Palpites dos times de casa: {palpitesTimeCasa1}, {palpitesTimeCasa2}")
print (f"Palpites dos times visitante: {palpitesTimeVisitante1}, {palpitesTimeVisitante2}")

for i in range (numeroPalpites):
    pontos = 0
    if golsTimesCasa[i] == palpitesTimeCasa1[i] and golsTimesFora[i] == palpitesTimeCasa2[i]:
        pontos = 3
    elif (golsTimesCasa[i] == palpitesTimeCasa1[i] and golsTimesFora[i] != palpitesTimeCasa2[i]) or (golsTimesCasa[i] != palpitesTimeCasa1[i] and golsTimesFora[i] == palpitesTimeCasa2[i]):
        pontos = 2
    elif (golsTimesCasa[i] - golsTimesFora[i] == palpitesTimeCasa1[i] - palpitesTimeCasa2[i]):
        pontos = 1
    else:
        pontos = 0
    
    pontuaçãoTotalCasa += pontos
    print (f"Pontuação do {timeCasa} no {i + 1}º jogo: {pontos}")

for i in range (numeroPalpites):
    pontos = 0
    if golsTimesCasa[i] == palpitesTimeVisitante1[i] and golsTimesFora[i] == palpitesTimeVisitante2[i]:
        pontos = 3
    elif (golsTimesCasa[i] == palpitesTimeVisitante1[i] and golsTimesFora[i] != palpitesTimeVisitante2[i]) or (golsTimesCasa[i] != palpitesTimeVisitante1[i] and golsTimesFora[i] == palpitesTimeVisitante2[i]):
        pontos = 2
    elif (golsTimesCasa[i] - golsTimesFora[i] == palpitesTimeVisitante1[i] - palpitesTimeVisitante2[i]):
        pontos = 1
    else:
        pontos = 0
    
    pontuaçãoTotalVisitante += pontos
    print (f"Pontuação do {timeVisitante} no {i + 1}º jogo: {pontos}")

print ("----------------------------------")
print ("----------------------------------")
print (f"Pontuação total do {timeCasa}: {pontuaçãoTotalCasa} pontos!")
print (f"Pontuação total do {timeVisitante}: {pontuaçãoTotalVisitante} pontos!")

if pontuaçãoTotalCasa > pontuaçãoTotalVisitante:
    print (f"O time {timeCasa} venceu!")
elif pontuaçãoTotalVisitante > pontuaçãoTotalCasa:
    print (f"O time {timeVisitante} venceu!")
elif pontuaçãoTotalCasa == pontuaçãoTotalVisitante:
    print ("Houve um empate no placar final!")
print ("----------------------------------")
print ("Obrigado por utilizar o validador de palpites, volte sempre!")