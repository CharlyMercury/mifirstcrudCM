from fastapi import FastAPI

app = FastAPI()

@app.get(path = "/home")
def home():
    return {"hellow":"CharlyMercury"}