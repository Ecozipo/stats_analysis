from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_spare():
    return {"Hello":"Spare"}
    

