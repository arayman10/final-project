#Final Project 
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
    cur.execute('CREATE TABLE IF NOT EXISTS Detroit_NBA (id INTEGER PRIMARY KEY, player_id INTEGER, weight INTEGER)')
    conn.commit()
    #url = 'https://www.balldontlie.io/api/v1/players/'

 
    """
    for player in data:
        player_weight = player['weight_pounds']
        #if player['id'] == 9:
            #new_lst.append(player_weight)
    
        NBA_id = player['id']
    #add_to_data = cur.execute('SELECT NBA_id FROM IDs WHERE NBA_id = ?', (NBA_id,)).fetchone()
    #if add_to_data is None:
    cur.execute('INSERT OR IGNORE INTO Detriotteams (NBA_id, weight) VALUES (?, ?)', (NBA_id, player_weight))
    conn.commit() 
    """   
    
    def main():
        #lst = readInData('https://www.balldontlie.io/api/v1/players/')
        cur, conn = setUpDatabase('nba.db')
        createNbaTable(cur, conn)
    main()
    