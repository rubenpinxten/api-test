from fastapi import FastAPI
import json
from pydantic import BaseModel

app = FastAPI()

application = {}

with open('./quotes.json') as csv_file:
    csv_file.readline()

    line = csv_file.readline()
    while line:
        application[line]
        line = csv_file

class Item(BaseModel):
    quote: str

@app.get("/quote/first")
async def get_first_quote():
    return application[0]

@app.get("/quote/last")
async def get_last_quote():
    return application[-1]

@app.post("/items/")
async def post_new_quote(item: Item):
    application = application + quote 
    with open('./quotes.json', mode='w', encoding='utf-8') as csv_file:
        json.dump(item, csv_file)
    return item