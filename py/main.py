from fastapi import FastAPI

app = FastAPI()

quotes = [
        {"Het leven is niet een kwestie van de beste kaarten hebben, maar eerder een slechte hand op de juiste manier weten te spelen."},
        {"Het beste bewijs van liefde is vertrouwen."},
        {"De beste vriend zal waarschijnlijk de beste echtgenote krijgen, omdat een goed huwelijk op een talent voor vriendschap berust."},
        {"Geduld id het beste gebed."},
        {"De beste manier om iets te leren is er les in te geven."},
        {"Water is het beste."},
        {"Tegenslag is de beste gelegenheid om te tonen dan men karakter heeft."},
        {"Als je voor elke positie de beste speler kiest, heb je nog geen sterk elftal maar een team dat als los zand uiteen valt."},
        {"De beste manier om zich op iemand te wreken is niet op hem te gelijken."},
        {"Opleiding is de beste proviand op de reis naar de ouderdom."}
        ]

@app.get("/quote/first")
async def get_first_quote():
    return quotes[0]

@app.get("/quote/last")
async def get_last_quote():
    return quotes[-1]
