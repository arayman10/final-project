import requests
import sqlite3
import os
import json
import time

#Red Wings players data https://records.nhl.com/site/api/player/byTeam/17

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/' + db_name)
    cur = conn.cursor()
    return cur, conn

def create_nhl_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS Detroit_NHL (id INTEGER PRIMARY KEY, player_name TEXT, weight INTEGER)')
    conn.commit()

def get_player_data():
    data = requests.get('https://records.nhl.com/site/api/player/byTeam/17')
    load_data = json.loads(data.text)
    #print(load_data)
    player_weight = {}
    for i in load_data["data"]:
        name = i['fullName']
        weight = i['weight']
        player_weight[name] = int(weight)
    return player_weight

def addPlayerWeightsToTable(cur, conn, dict):
    for i in dict.items():
        cur.execute('INSERT INTO Detroit_NHL (player_name, weight) VALUES (?, ?)', (i[0], i[1]))
    conn.commit()


def main():
    cur,conn = setUpDatabase('nhl.db')
    create_nhl_table(cur, conn)
    players_data = get_player_data()
    addPlayerWeightsToTable(cur, conn, players_data)
    
main()

