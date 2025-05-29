from fastapi import FastAPI
import redis
import services as db

app = FastAPI()

@app.get("/{lang}/{term}")
async def byLanguageAndTerm(lang: str, term: str):
    return { "etymology": db.get_by_language_and_term(lang, term) }

@app.get("")
async def byLanguageRandom(lang: str):
    return { "etymologies": db.get_randoms_by_langugage(lang) }

