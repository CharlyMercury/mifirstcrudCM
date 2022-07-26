from fastapi import FastAPI


users = []

app = FastAPI()


@app.get(path = "/")
def home():
    return {"Dedicado a Blanquita": "Hermosita"}


@app.get(
    path = "/users"
    )
def users_list():
    return users

@app.post(path = "/users")
def create_user():
    return {"hellow":"CharlyMercury"}


@app.put(path = "/users/{user_id}")
def update():
    return {"hellow":"CharlyMercury"}


@app.delete(path = "/users/{user_id}")
def delete():
    return {"hellow":"CharlyMercury"}


