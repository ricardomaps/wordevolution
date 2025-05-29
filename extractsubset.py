import csv

with open("etymology.csv") as rf:
    with open("subset.csv", "w") as wf: 
        fields = ["lang", "term", "related_lang", "related_term"]
        reader = csv.DictReader(rf)
        writer = csv.DictWriter(wf, fieldnames=fields)
        writer.writeheader()
        for row in reader:
            if row["reltype"] == "inherited_from":
                writer.writerow({ 
                    "lang": row["lang"],
                    "term": row["term"], 
                    "related_lang": row["related_lang"], 
                    "related_term": row["related_term"]})
