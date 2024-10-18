from fastapi import FastAPI
from stats.router import data

app = FastAPI()

@app.get("/")
def hello_spare():
    return {"Hello":"Spare"}
    

