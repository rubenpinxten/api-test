from fastapi import FastAPI
import json

app = FastAPI()

application = {}

with open('quotes.json') as csv_file:
    csv_file.readline()

    line = csv_file.readline()
    while line:
        application[line]
        line = csv_file

@app.get("/quote/first")
async def get_first_quote():
    return quotes[0]

@app.get("/quote/last")
async def get_last_quote():
    return quotes[-1]

