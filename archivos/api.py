from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Hola mundo"}

@app.get("/datos")
def saludo():
    return {"nombre": "Jorge Ambrosio", "Album": "Octopus"}