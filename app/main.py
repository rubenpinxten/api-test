from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = {"quotes": [{"quote": "Het leven is niet een kwestie van de beste kaarten hebben, maar eerder een slechte hand op de juiste manier weten te spelen."},
{"quote": "Het beste bewijs van liefde is vertrouwen."}, 
{"quote": "De beste vriend zal waarschijnlijk de beste echtgenote krijgen, omdat een goed huwelijk op een talent voor vriendschap berust."}, 
{"quote": "Geduld id het beste gebed."}, {"quote": "De beste manier om iets te leren is er les in te geven."}, 
{"quote": "Water is het beste."}, {"quote": "Tegenslag is de beste gelegenheid om te tonen dan men karakter heeft."}, 
{"quote": "Als je voor elke positie de beste speler kiest, heb je nog geen sterk elftal maar een team dat als los zand uiteen valt."}, 
{"quote": "De beste manier om zich op iemand te wreken is niet op hem te gelijken."}, 
{"quote": "Opleiding is de beste proviand op de reis naar de ouderdom."}]}

quote = {}

@app.get("/quote/first")
async def get_first_quote():
    return quotes[0]

@app.get("/quote/all")
async def get_all_quotes():
    return quotes

@app.get("/quote/last")
async def get_last_quote():
    tekst = quotes[-1]
    return tekst
@app.post("/quote/new/{tekst}")
async def new_quote(tekst: str):
    quote["quote"] = tekst
    quotes.append(quote)
    tekst = quotes[-1]
    return tekst