import json
filename = 'user_settings.txt'

myfile = open(filename,mode='w', encoding='latin_1')

player1 = {
    'PlayerName': "Donald",
    'Score': 345,
    'Awards': ['OR', 'NV', 'NY']
}

player2 = {
    'PlayerName': "Klinton",
    'Score': 370,
    'Awards': ['WT', 'TX', 'MI'],
    'Age': 47
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ================== Save by JSON ===================== #

json.dump(myplayers, myfile)

myfile.close()

# ================== Loas by JSON ====================== #

myfile = open(filename, mode='r')
configdata = json.load(myfile)
print(configdata)

for user in configdata:
    print("Player name is: " + str(user['PlayerName']))
    print("Player score is: " + str(user['Score']))
    for award in user['Awards']:
        print("Awards is: " + str(award))
    #print("Awards is: " + str(user['Awards'][0]))
    #print("Awards is: " + str(user['Awards'][1]))
    #print("Awards is: " + str(user['Awards'][2]))
    print("-------------------------------------")