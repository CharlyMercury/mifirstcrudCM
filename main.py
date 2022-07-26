from fastapi import FastAPI

app = FastAPI()

@app.get(path = "/home")
def home():
    return {"hellow":"CharlyMercury"}


@app.get(
    path = "/amoablanquita"
)
def amoablanquita():
    return {"holis":"Blaquita"}