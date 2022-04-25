import requests
import sqlite3
import os
import json
import csv


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
def sorting_weights(lst, filename):
    for i in player_weight:
        lst.append(i[1])
    lst = sorted(lst)
    min_max_tup = (lst[0], lst[-1])
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('The minimum and maximum weights of NBA players in the Detroit_NBA table', min_max_tup))
    file.close()
    return min_max_tup

def avg_weight(cur, conn, filename):
    cur.execute('SELECT AVG(weight) FROM Detroit_NBA')
    avg = cur.fetchone()[0]
    conn.commit()
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('The average weight of the NBA players in the Detroit_NBA table', avg))
    file.close()
    return avg

def main():
    cur, conn = setUpDatabase('final.db')
    createNbaTable(cur, conn)
    getPlayerData(player_weight)
    addPlayerWeightsToTable(cur, conn, player_weight)
    print(sorting_weights(weight_lst, 'calculations.txt'))
    print(avg_weight(cur, conn, 'calculations.txt'))
main()

import matplotlib.pyplot as plt
plt.hist(weight_lst, bins= 12, color= 'orange')
plt.xlim(170, 290)
#plt.hist(tigers_rosters_int, binedges= plt.xlim(160, 28))
plt.title("Weights of NBA Players", fontsize = 20)
plt.xlabel("Weight", fontsize= 14)
plt.ylabel("Count of Players", fontsize = 14)



plt.vlines(170, 0, 37, color = "black")
plt.vlines(180, 0, 37, color = "black")
plt.vlines(190, 0, 51, color = "black")
plt.vlines(200, 0, 69, color = "black")
plt.vlines(210, 0, 70, color = "black")
plt.vlines(220, 0, 73, color = "black")
plt.vlines(230, 0, 73, color = "black")
plt.vlines(240, 0, 55, color = "black")
plt.vlines(250, 0, 53, color = "black")
plt.vlines(260, 0, 28, color = "black")
plt.vlines(270, 0, 13, color = "black")
plt.vlines(280, 0, 9, color = "black")
plt.vlines(290, 0, 1, color = "black")

plt.hlines(16, 170, 180, color = "black")
plt.hlines(37, 180, 190, color = "black")
plt.hlines(51, 190, 200, color = "black")
plt.hlines(69, 200, 210, color = "black")
plt.hlines(70, 210, 220, color = "black")
plt.hlines(73, 220, 230, color = "black")
plt.hlines(55, 230, 240, color = "black")
plt.hlines(53, 240, 250, color = "black")
plt.hlines(28, 250, 260, color = "black")
plt.hlines(13, 260, 270, color = "black")
plt.hlines(9, 270, 280, color = "black")
plt.hlines(1, 280, 290, color = "black")
plt.show()






