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

def main():
    cur,conn = setUpDatabase('nhl.db')
    create_nhl_table(cur, conn)
    
main()

