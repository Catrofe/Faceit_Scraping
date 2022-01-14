from urllib.request import urlopen
from bs4 import BeautifulSoup
from update import InserirNoBanco

# Recebendo inputs
nickname = input("Qual seu nickname na faceit CS:GO?\n")

# Obtendo o HTML
response = urlopen(f"https://faceitstats.com/player/{nickname}")
html = response.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
name = soup.find("h1").getText().strip()
stats_divs = soup.findAll("div", {"class": "col-6 col-sm-6 col-md-4 col-lg-2"})

stats = []
for div in stats_divs:
    stats.append(div.find("h5").getText())

elo = int(stats[0])
all_matches = stats[1].split("/")
matches = int(all_matches[0].strip())
won = int(all_matches[1].strip())
lost = int(all_matches[2].strip())
win_rate = int(stats[2].replace("%", ""))
kd = float(stats[3])
hs_rate = int(stats[4].replace("%", ""))
win_streak = int(stats[5])

InserirNoBanco(name, elo, matches, won, lost, win_rate, kd, hs_rate, win_streak)
