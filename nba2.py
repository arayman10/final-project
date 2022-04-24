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

weight_lst = []
def get_avg_weight(lst):
    for i in player_weight:
        lst.append(i[1])
    print(sorted(lst))
    count = len(lst)
    total_weight = 0
    for number in lst:
        total_weight += int(number)
    avg_weight = total_weight/count
    print(avg_weight)
    return avg_weight

import matplotlib.pyplot as plt
plt.hist(weight_lst, bins= 12)
plt.xlim(165, 295)
#plt.hist(tigers_rosters_int, binedges= plt.xlim(160, 280))
plt.title("Weights of NBA Players", fontsize = 20)
plt.xlabel("Weight", fontsize= 14)
plt.ylabel("Count of Players", fontsize = 14)
'''
plt.vlines(170, 0, 1, color = "orange")
plt.vlines(180, 0, 3, color = "orange")
plt.vlines(190, 0, 6, color = "orange")
plt.vlines(200, 0, 7, color = "orange")
plt.vlines(210, 0, 7, color = "orange")
plt.vlines(220, 0, 6, color = "orange")
plt.vlines(230, 0, 6, color = "orange")
plt.vlines(240, 0, 4, color = "orange")
plt.vlines(250, 0, 2, color = "orange")
plt.vlines(260, 0, 1, color = "orange")
plt.vlines(270, 0, 2, color = "orange")

plt.hlines(1, 160, 180, color = "orange")
plt.hlines(3, 180, 190, color = "orange")
plt.hlines(6, 190, 200, color = "orange")
plt.hlines(7, 200, 210, color = "orange")
plt.hlines(6, 210, 230, color = "orange")
plt.hlines(4, 230, 240, color = "orange")
plt.hlines(2, 240, 250, color = "orange")
plt.hlines(1, 250, 270, color = "orange")
plt.hlines(2, 270, 280, color = "orange")
plt.show()
'''

def main():
    cur, conn = setUpDatabase('nba.db')
    createNbaTable(cur, conn)
    getPlayerData(player_weight)
    addPlayerWeightsToTable(cur, conn, player_weight)
    get_avg_weight(weight_lst)
main()


