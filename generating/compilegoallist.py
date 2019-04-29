import json
import csv

goallist = [[] for i in range(25)]
with open('goallist.csv') as glf:
    goalreader = csv.reader(glf)
    for goal in list(goalreader)[1:]:
        # ignore empty space
        if goal[0].strip() != '':
            # filter out all non shrine/korok goals
            # if not ('Shrine' in goal[1] or 'Korok' in goal[1] or 'Side Quest' in goal[1] or 'Dogreward' in goal[1]):
            #    continue
            difficulty = int(goal[3])
            goal = {'name':goal[0], 'jp':goal[1], 'types':goal[2].split(',')}
            goallist[difficulty].append(goal)

# dump the json into a js function for easy import
with open('../tables/normal_v2.json','w',encoding='utf8') as bf:
    #bf.write('var bingoList = ')
    json.dump(goallist, bf, ensure_ascii=False, indent=4)
    #bf.write(';')
