import csv

ALLREGIONS=["Plateau","Central Hyrule","Hateno","Faron","Ridgeland","Lake","Wasteland","Woodland","Lanayru","Eldin","Akkala","Tabantha","Gerudo","Hebra","Dueling Peaks"]

allgoals = []

with open('goallist.csv','r') as f:
    reader = csv.reader(f)
    allgoals = list(reader)

for goal in allgoals:
    synergies = set(goal[1].split(','))
    if 'Shrine' in synergies and not 'Shrine Quest' in synergies:
        regionsynergies = synergies.intersection(ALLREGIONS)
        if len(regionsynergies) == 0:
            synergies.remove('Shrine')
            for reg in ALLREGIONS:
                synergies.add(reg+' Shrine')
        else:
            synergies.remove('Shrine')
            regsyn = regionsynergies.pop()
            synergies.add(regsyn+' Shrine')
        goal[1]=','.join(synergies)

with open('goallistws.csv','w') as f:
    writer = csv.writer(f)
    for goal in allgoals:
        writer.writerow(goal)
