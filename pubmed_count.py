import json

with open('mergedCOIS_121719.json') as f:
    data = json.load(f)

pmids = []

for row in data:
    pmid = row['pmid']
    pmids.append(pmid)

print (len(pmids))


