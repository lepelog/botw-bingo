import csv
import json

translation = {}
with open('../tables/normal_v1.json','r') as f:
    readjson = json.load(f)
    for difficulty in readjson:
        for goal in difficulty:
            translation[goal["name"]]=goal["jp"]

alllines=[]
with open('goallist.csv','r') as f:
    reader = csv.reader(f)
    for line in reader:
        transl = line[0]
        if transl in translation:
            transl = translation[transl]
        line.insert(1, transl)
        alllines.append(line)

with open('goallistjp.csv','w') as f:
    writer = csv.writer(f)
    for line in alllines:
        writer.writerow(line)
