#Final Project 
import requests
import sqlite3
import os
import json
import time

def readInData(url):
    for i in range(1, 38):
        query = {'per_page': '100', 'page': str(i)}
        resp = requests.get(url, params = query)
        data = resp.text
        lst = json.loads(data)['data']  
    return lst  
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/' + db_name)
    cur = conn.cursor()
    return cur, conn

def createWeightTable(data, cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS Detriotteams (id INTEGER PRIMARY KEY, NBA_id INTEGER UNIQUE, weight INTEGER')
    #url = 'https://www.balldontlie.io/api/v1/players/'

    #count = 0 
    '''
    for i in range(1, 38):
        query = {'per_page': '100', 'page': str(i)}
        resp = requests.get(url, params = query)
        data = resp.text
        lst = json.loads(data)['data']
        new_lst = []
        '''

    for player in data:
        player_weight = player['weight_pounds']
        #if player['id'] == 9:
            #new_lst.append(player_weight)
    
    NBA_id = player['id']
    #add_to_data = cur.execute('SELECT NBA_id FROM IDs WHERE NBA_id = ?', (NBA_id,)).fetchone()
    #if add_to_data is None:
    cur.execute('INSERT OR IGNORE INTO Detriotteams (NBA_id, weight) VALUES (?, ?)', (NBA_id, player_weight))
    conn.commit()    
    
    def main():
        lst = readInData('https://www.balldontlie.io/api/v1/players/')
        cur, conn = setUpDatabase('detriotteams.db')
        createWeightTable(lst, cur, conn)
    main()
    