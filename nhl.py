import requests
import sqlite3
import os
import json
import time
import matplotlib.pyplot as plt

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/' + db_name)
    cur = conn.cursor()
    return cur, conn

def create_nhl_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS Detroit_NHL (id INTEGER PRIMARY KEY, player_name TEXT, weight INTEGER, team_id INTEGER)')
    conn.commit()

def create_team_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS TeamNames (id INTEGER PRIMARY KEY, team TEXT, data_id INTEGER)')
    conn.commit()

def team_data(cur, conn):
    data = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
    load_data = json.loads(data.text)   
    teams = []
    for x in load_data["teams"]:
        id = x['id']
        name = x['name']
        teams.append((id,name))
    count = 0
    for i in range(len(teams)):
        if count > 24:
            break
        if cur.execute('SELECT team FROM TeamNames WHERE team = ? AND data_id = ?', (teams[i][1], teams[i][0])).fetchone() == None:
            cur.execute('INSERT OR IGNORE INTO TeamNames (team, data_id) VALUES (?, ?)', (teams[i][1], teams[i][0]))
            count += 1
    conn.commit()
    return teams

def get_player_data(cur, conn):
    data = requests.get('https://records.nhl.com/site/api/player')
    load_data = json.loads(data.text)
    player_weight = []
    for i in range(275):
        dict = load_data["data"][i]
        name = dict['fullName']
        weight = dict['weight']
        team_num = dict['careerTeamId']
        tup = (name, weight, team_num)
        player_weight.append(tup)
    new_player_weight = []
    for item in player_weight:
        cur.execute('SELECT id, data_id FROM TeamNames')
        for row in cur:
            if item[2] == row[1]:
                team_id = row[0]
                new_player_weight.append((item[0], item[1], item[2], team_id))
    conn.commit()    
    return new_player_weight

def addPlayerWeightsToTable(cur, conn, tup_lst):
    count = 0
    for i in range(len(tup_lst)):
        if count > 24:
            break
        if cur.execute('SELECT player_name FROM Detroit_NHL WHERE player_name = ? AND weight = ? AND team_id = ?', (tup_lst[i][0], tup_lst[i][1], tup_lst[i][3])).fetchone() == None:
            cur.execute('INSERT OR IGNORE INTO Detroit_NHL (player_name, weight, team_id) VALUES (?, ?, ?)', (tup_lst[i][0], tup_lst[i][1], tup_lst[i][3]))
            count += 1
    conn.commit()

def get_avg_weight(players_data):   
    weight_lst = []
    for i in players_data:
        weight = i[1]
        weight_lst.append(weight)
    print(sorted(weight_lst))
    count = len(weight_lst)
    total_weight = 0
    for number in weight_lst:
        total_weight += int(number)
    avg_weight = total_weight/count
    print(avg_weight)
    return avg_weight

def avg_weight(cur, conn):
    cur.execute('SELECT AVG(weight) FROM Detroit_NHL')
    avg = cur.fetchone()[0]
    conn.commit()
    return avg

team_count = {}

def players_per_team(dict, num, cur, conn):
    cur.execute('SELECT TeamNames.team FROM Detroit_NHL JOIN TeamNames ON Detroit_NHL.team_id = TeamNames.id WHERE Detroit_NHL.team_id = ?', (num,))
    team = cur.fetchall()
    if len(team) > 0:
        dict[team[0][0]] = 0
        for player in team:
            dict[team[0][0]] += 1
    conn.commit()
    return None

#create pie chart
labels = 'New York Rangers', 'Philadelphia Flyers', 'Pittsburgh Penguins', 'Boston Bruins', 'Montréal Canadiens', 'Toronto Maple Leafs', 'Washington Capitals', 'Chicago Blackhawks', 'Detroit Red Wings', 'St. Louis Blues', 'Edmonton Oilers', 'Vancouver Canucks', 'Los Angeles Kings'
sizes = [16, 2, 3, 17, 15, 20, 3, 13, 15, 1, 1, 2, 2]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', labeldistance=0.85, radius=5)
plt.title("Players Per NHL Team")
plt.axis('equal')
plt.show()

def main():
    cur,conn = setUpDatabase('final.db')
    #create_nhl_table(cur, conn)
    #create_team_table(cur,conn)
    #teams = team_data(cur,conn)
    players_data = get_player_data(cur, conn)
   #addPlayerWeightsToTable(cur, conn, players_data)
    get_avg_weight(players_data)
    print(avg_weight(cur, conn))
    #for num in range(len(teams)):
        #players_per_team(team_count, num+1, cur, conn)
    #print(team_count)
    
main()
#Histogram
import matplotlib.pyplot as plt
plt.hist(weight_lst, bins= 12, color = 'red', edgecolor= 'black', linewidth= 1.2)
plt.xlim(145, 285)
#plt.hist(tigers_rosters_int, binedges= plt.xlim(160, 280))
plt.title("Weights of NHL Players ", fontsize = 20)
plt.xlabel("Weight", fontsize= 14)
plt.ylabel("Count of Players", fontsize = 14)

