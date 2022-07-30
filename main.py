from fastapi import FastAPI
from routes.user import users


app = FastAPI()
app.include_router(users)


@app.get(path = "/")
def home():
    return {"Dedicado a Blanquita": "Hermosita"}

