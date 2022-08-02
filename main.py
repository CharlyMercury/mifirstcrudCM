from fastapi import FastAPI
from routes.user import usersapp


app = FastAPI()
app.include_router(usersapp)


@app.get(path = "/")
def home():
    return {"Dedicado a Blanquita": "Hermosita"}

