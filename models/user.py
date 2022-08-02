from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta
from config.db import engine

users = Table(
    "users", 
    meta, 
    Column("id", Integer, primary_key=True),
    Column("username", String(20)),
    Column("password", String(20)),
    Column("email", String(20)),
    Column("fullname", String(100)),
    Column("roll", String(20)),
    Column("address", String(100)),
    Column("city", String(30)),
    Column("country", String(30)),
    Column("postal_code", String(30)),
    Column("cel_number", String(30))
)

meta.create_all(engine)