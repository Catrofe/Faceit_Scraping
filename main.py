from urllib.request import urlopen
from bs4 import BeautifulSoup
from update import InserirNoBanco, LerBanco

# Recebendo inputs
nickname = input("Qual seu nickname na faceit CS:GO?\n")

## Obtendo o HTML e o total de páginas
response = urlopen("https://faceitstats.com/player/" + nickname)
html = response.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
name = soup.find("h1").getText().strip()
dados = soup.findAll("div", {"class": "col-6 col-sm-6 col-md-4 col-lg-2"})

soup.findAll("div", {"class": "col-6 col-sm-6 col-md-4 col-lg-2"})
lista = []
for item in dados:
    lista.append(item.find("h5").getText())

elo = int(lista[0])
Matches = lista[1]
win_rate = int(lista[2].replace("%", ""))
kd = float(lista[3])
hs_rate = int(lista[4].replace("%", ""))
win_streak = int(lista[5])
Matches = Matches.split("/")
matches = int(Matches[0].strip())
won = int(Matches[1].strip())
lost = int(Matches[2].strip())


InserirNoBanco(name, elo, matches, won, lost, win_rate, kd, hs_rate, win_streak)


# NOME, ELO, MATCHES, WON, LOST, WINRATE, KD, HS_RATE, WINSTREAK
