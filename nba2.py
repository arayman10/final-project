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


player_weight = {}

def getPlayerData(dict):
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
                dict[full_name] = int(weight)
            except:
                print('Not a number')
    return None

def addPlayerWeightsToTable(cur, conn, dict):
    for i in dict.items():
        cur.execute('INSERT INTO Detroit_NBA (player_name, weight) VALUES (?, ?)', (i[0], i[1]))
    conn.commit()
def main():
    cur, conn = setUpDatabase('nba2.db')
    createNbaTable(cur, conn)
    getPlayerData(player_weight)
    addPlayerWeightsToTable(cur, conn, player_weight)
main()


