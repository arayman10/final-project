import requests
import json
'''
def get_tigers_weight_data(player):
    base_url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part=" + "'" + player + "'"
    res = requests.get(base_url)
    data = json.loads(res.text)
    return data['search_player_all']['queryResults']['row']
    
data = (get_tigers_weight_data('jason foley'))
'''
def get_tigers_players():
    base_url = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='116'"
    res = requests.get(base_url)
    data = json.loads(res.text)
    new_lst = data['roster_40']['queryResults']['row']
    weight_list = []
    for item in new_lst:
       weight_list.append(item['weight'])
    return weight_list
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


#GRAPHING
import matplotlib.pyplot as plt
plt.hist(tigers_rosters_int, bins= 12)
plt.xlim(160, 280)
#plt.hist(tigers_rosters_int, binedges= plt.xlim(160, 280))
plt.title("Weights of Detroit Tigers Players", fontsize = 20)
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