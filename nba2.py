import requests
import sqlite3
import os
import json
import time

 

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/' + db_name)
    cur = conn.cursor()
    return cur, conn

def createNbaTable(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS Detroit_NBA (id INTEGER PRIMARY KEY, player_name TEXT, weight INTEGER)')
    conn.commit()


player_weight = []

def getPlayerData(lst):
    for i in range(1,38):
        querystring = {'per_page': '100', 'page': str(i)}
        resp = requests.get('https://www.balldontlie.io/api/v1/players/', params=querystring)
        data = json.loads(resp.text)
        for i in data['data']:
            first = i["first_name"]
            last = i["last_name"]
            full_name = first + " " + last
            weight = i["weight_pounds"]
            try:
                lst.append((full_name, int(weight)))
            except:
                None
    return None

def addPlayerWeightsToTable(cur, conn, lst):
    count = 0
    for i in range(len(lst)):
        if count > 24:
            break
        if cur.execute('SELECT player_name FROM Detroit_NBA WHERE player_name = ? AND weight = ?', (lst[i][0], lst[i][1])).fetchone() == None:
            cur.execute('INSERT OR IGNORE INTO Detroit_NBA (player_name, weight) VALUES (?, ?)', (lst[i][0], lst[i][1]))
            count += 1
    conn.commit()
def main():
    cur, conn = setUpDatabase('nba.db')
    createNbaTable(cur, conn)
    getPlayerData(player_weight)
    addPlayerWeightsToTable(cur, conn, player_weight)
    print(player_weight)
main()


