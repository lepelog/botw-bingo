import json
import csv

goallist = [[] for i in range(25)]
with open('goallist.csv') as glf:
    goalreader = csv.reader(glf)
    for goal in list(goalreader)[1:]:
        # ignore empty space
        if goal[0].strip() != '':
            difficulty = int(goal[2])
            goal = {'name':goal[0], 'types':goal[1].split(',')}
            goallist[difficulty].append(goal)

with open('board.js','w') as bf:
    bf.write('var bingoList = ')
    json.dump(goallist, bf)
    bf.write(';\n  $(function () { srl.bingo(bingoList, 5); });')
