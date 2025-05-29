import redis

r = redis.Redis()

def remove_duplicates(etymology):
    langs = set()
    for i in range(len(etymology)):
        if etymology[i]["lang"] in langs:
            return etymology[:i]
        langs.add(etymology[i]["lang"])
    return etymology

def parse_to_dict(etymology):
    for i in range(len(etymology)):
        old_language, old_word = etymology[i].decode("utf-8").split(":")
        etymology[i] = { "lang": old_language, "term": old_word }
    return etymology

def get_by_language_and_term(lang: str, term: str):
    etymology = r.lrange(lang + ":" + term, 0, -1)
    return parse_to_dict(etymology)

def get_randoms_by_language(lang: str):
    keys = [r.randomkey() for _ in range(20)]
    etymologies = [r.lrange(key, 0, -1) for key in keys]
    return list(map(parse_to_dict, etymologies))
