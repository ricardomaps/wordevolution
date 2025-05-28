from fastapi import FastAPI
import redis

r = redis.Redis()
app = FastAPI()

@app.get("/{lang}/{term}")
async def root(lang: str, term: str):
    etymology = r.lrange(lang + ":" + term, 0, -1)
    for i in range(len(etymology)):
        old_language, old_word = etymology[i].decode("utf-8").split(":")
        etymology[i] = { "lang": old_language, "term": old_word }
    return { "etymology": etymology }
