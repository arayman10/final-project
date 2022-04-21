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

def getPlayerData():
    resp = requests.get('https://www.balldontlie.io/api/v1/players/')
    data = json.loads(resp.text)
    print(data)
    dict = {}
    
    

def main():
    cur, conn = setUpDatabase('nba.db')
    createNbaTable(cur, conn)
    getPlayerData()
main()