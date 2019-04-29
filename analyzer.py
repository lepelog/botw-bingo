import subprocess
import json
import random

COMMAND='{{ cat js/bingo.js js/seedrandom-min.js tables/board.js; echo "console.log(JSON.stringify(getBingoBoard(bingoList, 5, {{seed:{}}})))"; }} | node'

goalcounts = {}
typecounts = {}

for i in range(100):
    seed = random.randint(0,999999)
    raw_out = subprocess.check_output(['sh', '-c', COMMAND.format(seed)])
    card = json.loads(raw_out.decode('utf-8'))[1:]
    for goal in card:
        if goal["name"] in goalcounts:
            goalcounts[goal["name"]] += 1
        else:
            goalcounts[goal["name"]] = 1
        for typ in goal["types"]:
            if typ in typecounts:
                typecounts[typ] += 1
            else:
                typecounts[typ] = 1
    if (i%10) == 0:
        print('{} done'.format(i)) 
print("\ngoalcounts:")
sorted_goalcounts = sorted(goalcounts.items(), key=lambda k: k[1], reverse=True)
for goal in sorted_goalcounts:
    print("{}: {}".format(goal[1], goal[0]))

print("\ntypecounts:")
sorted_typecounts = sorted(typecounts.items(), key=lambda k: k[1], reverse=True)
for typ in sorted_typecounts:
    print("{}: {}".format(typ[1], typ[0]))
