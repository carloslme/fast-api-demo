from enum import Enum
from fastapi import FastAPI

# Enum class that will list the different types of users
class UserType(str, Enum):
    STANDARD = "STANDARD"
    admin = "admin"

app = FastAPI()

@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id:int):
    return {"type":type ,"id": id}