import csv
import json
from collections import defaultdict

db = {}

sort_order = {"Proto-Indo-European": 0,
              "Proto-Germanic": 1,
              "Proto-West Germanic": 2, 
              "Old English": 3,
              "Northern Middle English": 5,
              "Middle English": 4}

with open("subset.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["lang"] == "English" and '-' not in row["term"]:
            key = row["term"]
            val = {"language": row["related_lang"], "word": row["related_term"]}
            if key not in db:
                db[key] = []
            db[key].append(val)

etymology = [list(sorted(ety, key=lambda x: sort_order[x["language"]])) + [{"language": "English", "word": word}] for word, ety in db.items() if len(ety) >= 3]

with open("db.json", "w") as db:
    json.dump(etymology, db)
