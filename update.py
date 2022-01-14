import mysql.connector
import datetime


def AbreDB():
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2020abcd",
    database="faceit"
  )
  cursor = connection.cursor()
  return connection

def InserirNoBanco(nome, elo, matches, won, lost, winrate, kd, hs_rate, winstreak):
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2020abcd",
    database="faceit"
  )
  cursor = connection.cursor()

  sql = f"""INSERT INTO tbfaceituser (NOME, ELO, MATCHES, WON, LOST, WINRATE, KD, HS_RATE, WINSTREAK) 
  VALUES('{nome}', {elo}, {matches}, {won}, {lost}, {winrate}, {kd}, {hs_rate}, {winstreak});"""
                                                                                               
  data = (
    'Primeiro Usuário',
    'primeirousuario@teste.com.br',
    datetime.datetime.today()
  )
  print(sql)
  cursor.execute(sql)
  connection.commit()

  userid = cursor.lastrowid

  cursor.close()
  connection.close()

  print("Foi cadastrado o novo usuário de ID:", userid)

def LerBanco():
  connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2020abcd",
  database="faceit"
)

  cursor = connection.cursor()

  sql = "SELECT * FROM tbfaceituser"

  cursor.execute(sql)
  results = cursor.fetchall()

  cursor.close()
  connection.close()

  print("ID, NOME, ELO, MATCHES, WON, LOST, WINRATE, KD, HS_RATE, WINSTREAK")
  for result in results:
    print(result)
