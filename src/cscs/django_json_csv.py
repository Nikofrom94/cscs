
import json
import csv

input = '/home/niko/Documents/jdr/CypherSystem/Cypher-SRD-FR/CSCG/cscg-20260217.json'

with open(input,'r') as json_file:
    data = json.load(json_file)

excluded = [
    'pub_date',
    'created',
    'updated',
    'stat_cost',
    'name',
    'description',
    'stat'
]

ab_fieldnames = [
    'id',
    'name_en',
    'cs_page',
    'tier',
    'categories'
]

with open('./output.csv','w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file,fieldnames=ab_fieldnames)
    writer.writeheader()
    for row in data:
        if row['model'] == "cscg.ability":
            newrow = {'id' : row['pk']}
            for key in row['fields'].keys():
                if key != 'categories' and key not in excluded:
                    newrow[key] = row['fields'][key]
            newrow['categories'] = ','.join([str(c) for c in row['fields']['categories']])
            writer.writerow(newrow)