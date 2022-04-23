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
    for i in range(25):
        dict = load_data["data"][i]
        name = dict['fullName']
        weight = dict['weight']
        tup = (name, weight)
        player_weight.append(tup)
    print(player_weight)
    return player_weight

#def addPlayerWeightsToTable(cur, conn, tup_lst):
    #for i in tup_lst:
        #cur.execute('INSERT INTO Detroit_NHL (player_name, weight) VALUES (?, ?)', (i[0], i[1]))
    #conn.commit()


def main():
    cur,conn = setUpDatabase('nhl.db')
    create_nhl_table(cur, conn)
    get_player_data()
    #addPlayerWeightsToTable(cur, conn, players_data)
    
main()

