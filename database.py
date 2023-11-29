import mysql.connector


def conecta():
    return mysql.connector.connect(
        host="localhost", user="root", password="2020abcd", database="faceit"
    )


def insere_stats(nome, elo, matches, won, lost, winrate, kd, hs_rate, winstreak):
    connection = conecta()
    cursor = connection.cursor()

    sql = f"""INSERT INTO tbfaceituser (NOME, ELO, MATCHES, WON, LOST, WINRATE, KD, HS_RATE, WINSTREAK) 
  VALUES('{nome}', {elo}, {matches}, {won}, {lost}, {winrate}, {kd}, {hs_rate}, {winstreak});"""

    cursor.execute(sql)
    connection.commit()

    userid = cursor.lastrowid

    cursor.close()
    connection.close()

    print("Foi cadastrado o novo usuário de ID:", userid)


def le_stats():
    connection = conecta()
    cursor = connection.cursor()

    sql = "SELECT * FROM tbfaceituser"

    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    print("ID, NOME, ELO, MATCHES, WON, LOST, WINRATE, KD, HS_RATE, WINSTREAK")
    for result in results:
        print(result)
