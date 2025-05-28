import csv
import redis

langs = { "English", "French", "Portuguese", "Spanish", "German", "Dutch", "Italian", "Romanian" }
rels = { "inherited_from" }

db = redis.Redis()

with open("etymology.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["lang"] not in langs: continue
        if row["reltype"] not in rels: continue
        
        key = row["lang"] + ":" + row["term"]
        val = row["related_lang"] + ":" + row["related_term"]
        db.lpush(key, val)
    print(db.lrange("English:cat", 0, -1))
