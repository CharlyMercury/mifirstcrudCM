from fastapi import APIRouter 


users = APIRouter()


@users.get(
    path = "/users"
    )
def users_list():
    return {"hellow":"CharlyMercury"}


@users.post(path = "/users")
def create_user():
    return {"hellow":"CharlyMercury"}


@users.put(path = "/users/{user_id}")
def update():
    return {"hellow":"CharlyMercury"}


@users.delete(path = "/users/{user_id}")
def delete():
    return {"hellow":"CharlyMercury"}

