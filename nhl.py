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
    data = requests.get('https://records.nhl.com/site/api/player')
    load_data = json.loads(data.text)
    player_weight = []
    for i in range(150):
        dict = load_data["data"][i]
        name = dict['fullName']
        weight = dict['weight']
        tup = (name, weight)
        player_weight.append(tup)
    return player_weight

def addPlayerWeightsToTable(cur, conn, tup_lst):
    count = 0
    for i in range(len(tup_lst)):
        if count > 24:
            break
        if cur.execute('SELECT player_name FROM Detroit_NHL WHERE player_name = ? AND weight = ?', (tup_lst[i][0], tup_lst[i][1])).fetchone() == None:
            cur.execute('INSERT OR IGNORE INTO Detroit_NHL (player_name, weight) VALUES (?, ?)', (tup_lst[i][0], tup_lst[i][1]))
            count += 1
    conn.commit()

def main():
    cur,conn = setUpDatabase('nhl.db')
    create_nhl_table(cur, conn)
    players_data = get_player_data()
    addPlayerWeightsToTable(cur, conn, players_data)
    
main()

