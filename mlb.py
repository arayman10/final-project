import requests
import json
import os
import sqlite3
'''
def get_tigers_weight_data(player):
    base_url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part=" + "'" + player + "'"
    res = requests.get(base_url)
    data = json.loads(res.text)
    return data['search_player_all']['queryResults']['row']
    
data = (get_tigers_weight_data('jason foley'))
'''
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/' + db_name)
    cur = conn.cursor()
    return cur, conn

def createMlbTable(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS MLB_Players (id INTEGER PRIMARY KEY, player_name TEXT, weight INTEGER)')
    conn.commit()

tigers_player_weight = []

def get_tigers_players(lst):
    base_url = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='116'"
    res = requests.get(base_url)
    data = json.loads(res.text)
    for i in data['roster_40']['queryResults']['row']:
        first = i['name_first']
        last = i['name_last']
        total = first + ' ' + last
        weight = i['weight']
        try:
            lst.append((total, int(weight)))
        except:
            None
    return None

yankees_player_weight = []

def get_yankees_player(lst):
    base_url = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='147'"
    res = requests.get(base_url)
    data = json.loads(res.text)
    for i in data['roster_40']['queryResults']['row']:
        first = i['name_first']
        last = i['name_last']
        total = first + ' ' + last
        weight = i['weight']
        try:
            lst.append((total, int(weight)))
        except:
            None
    return None

dodgers_player_weight = []
def get_dodgers_player(lst):
    base_url = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='119'"
    res = requests.get(base_url)
    data = json.loads(res.text)
    for i in data['roster_40']['queryResults']['row']:
        first = i['name_first']
        last = i['name_last']
        total = first + ' ' + last
        weight = i['weight']
        try:
            lst.append((total, int(weight)))
        except:
            None
    return None


'''
    new_lst = data['roster_40']['queryResults']['row']
    weight_list = []
    for item in new_lst:
       weight_list.append(item['weight'])
    '''
'''    
tigers_rosters = get_tigers_players()
#print(tigers_rosters)
count = len(tigers_rosters)
total_weight = 0
tigers_rosters_int = []
for number in tigers_rosters:
    total_weight += int(number)
    tigers_rosters_int.append(int(number))
#print(total_weight)
tigers_avg_weight = total_weight/count
'''
def add_to_table(cur, conn, lst):
    count = 0
    for i in range(len(lst)):
        if count > 7:
            break
        if cur.execute('SELECT player_name FROM MLB_Players WHERE player_name = ? AND weight = ?', (lst[i][0], lst[i][1])).fetchone() == None:
            cur.execute('INSERT OR IGNORE INTO MLB_Players (player_name, weight) VALUES (?, ?)', (lst[i][0], lst[i][1]))
            count += 1
    conn.commit()

def add_to_table2(cur, conn, lst):
    count = 0
    for i in range(len(lst)):
        if count > 7:
            break
        if cur.execute('SELECT player_name FROM MLB_Players WHERE player_name = ? AND weight = ?', (lst[i][0], lst[i][1])).fetchone() == None:
            cur.execute('INSERT OR IGNORE INTO MLB_Players (player_name, weight) VALUES (?, ?)', (lst[i][0], lst[i][1]))
            count += 1
    conn.commit()

def add_to_table3(cur, conn, lst):
    count = 0
    for i in range(len(lst)):
        if count > 7:
            break
        if cur.execute('SELECT player_name FROM MLB_Players WHERE player_name = ? AND weight = ?', (lst[i][0], lst[i][1])).fetchone() == None:
            cur.execute('INSERT OR IGNORE INTO MLB_Players (player_name, weight) VALUES (?, ?)', (lst[i][0], lst[i][1]))
            count += 1
    conn.commit()

weight_lst = []
def get_avg_weight(lst):
    for i in tigers_player_weight:
        lst.append(i[1])
    for i in yankees_player_weight:
        lst.append(i[1])
    for i in dodgers_player_weight:
        lst.append(i[1])
    print(sorted(lst))
    count = len(lst)
    total_weight = 0
    for number in lst:
        total_weight += int(number)
    avg_weight = total_weight/count
    print(avg_weight)
    return avg_weight

#GRAPHING
import matplotlib.pyplot as plt
plt.hist(weight_lst, bins= 12, color= 'green')
plt.xlim(160, 280)
#plt.hist(tigers_rosters_int, binedges= plt.xlim(160, 280))
plt.title("Weights of MLB Players", fontsize = 20)
plt.xlabel("Weight", fontsize= 14)
plt.ylabel("Count of Players", fontsize = 14)

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


#BAR CHART SAMPLE
import matplotlib.pyplot as plt
tigers_avg_weight = 214.5
pistons_avg_weight = 220
redwings_avg_weight = 280
x_title = ["Tigers", "Pistons", "Red Wings"]
y_title = [tigers_avg_weight, pistons_avg_weight, redwings_avg_weight]
color_lst = ["orange", "blue", "red"]
plt.title("Average Player Weights of Detroit's Major League Sports Teams", fontsize= 13)
plt.xlabel("Team", fontsize = 12 )
plt.ylabel("Average Player Weight", fontsize= 12)
plt.bar(x_title, y_title, color = color_lst)
plt.show()


def main():
    cur, conn = setUpDatabase('final.db')
    createMlbTable(cur, conn)
    get_tigers_players(tigers_player_weight)
    get_yankees_player(yankees_player_weight)
    get_dodgers_player(dodgers_player_weight)
    add_to_table(cur,conn,tigers_player_weight)
    add_to_table2(cur,conn,yankees_player_weight)
    add_to_table3(cur,conn,dodgers_player_weight)
    get_avg_weight(weight_lst)
main()
