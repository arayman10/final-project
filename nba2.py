import requests
import sqlite3
import os
import json
import time

from sklearn.preprocessing import PolynomialFeatures
 

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/' + db_name)
    cur = conn.cursor()
    return cur, conn

def createNbaTable(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS Detroit_NBA (id INTEGER PRIMARY KEY, player_name TEXT, weight INTEGER)')
    conn.commit()
lst = ['Bagley', 'Saddiq', 'Cunningham', 'Hamidou', 'Carsen', 'Garza', 'Jerami', 'Killian', 'Frank', 'Joseph', 'Braxton', 'Saben', 'Livers', 'McGruder', 'Olynyk', 'Jamorko', 'Stewart']
full_names = ['Marvin Bagley III', 'Saddiq Bey', 'Cade Cunningham', 'Hamidou Diallo', 'Carsen Edwards', ' Luka Garza', 'Jerami Grant', 'Killian Hayes', 'Frank Jackson', 'Cory Joseph', 'Braxton Key', 'Saben Lee', 'Isaiah Livers', 'Rodney McGruder', 'Kelly Olynyk', 'Jamorko Pickett', 'Isaiah Stewart']

players = {}

def getPlayerData(full_name, single, dict):
    
    resp = requests.get(f'https://www.balldontlie.io/api/v1/players/?search={single}')
    data = json.loads(resp.text)
    for i in data['data']:
        first = i["first_name"]
        last = i["last_name"]
        total = first + " " + last
        if full_name == total:
            weight = i["weight_pounds"]
            dict[full_name] = weight
    return None

def addPlayerWeightsToTable(cur, conn, dict):
    for i in dict.items():
        cur.execute('INSERT INTO Detroit_NBA (player_name, weight) VALUES (?, ?)', (i[0], i[1]))
    conn.commit()
def main():
    cur, conn = setUpDatabase('nba.db')
    createNbaTable(cur, conn)
    for i in range(len(full_names)):
        getPlayerData(full_names[i], lst[i], players)
    addPlayerWeightsToTable(cur, conn, players)
main()

print(players)
