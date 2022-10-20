from enum import Enum
from fastapi import FastAPI, Query


class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"    

app = FastAPI()

@app.get("/users")
async def get_user(format: UsersFormat):
    return {"format":format}

@app.get("/user")
async def get_user_ad(page: int=Query(1, gt=0), size:int=Query(10, le=100)):
    return {"page":page, "size":size}