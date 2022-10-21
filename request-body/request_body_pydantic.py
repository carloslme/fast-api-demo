"""
Defining payload validations like JSON has some major drawbacks. 
First, it's quite verbose and makes the path operation function prototype huge, 
especially for bigger models. Second, usually, you'll need to reuse the 
data structure on other endpoints or in other parts of your application.
"""
from fastapi import FastAPI, Body
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str

app = FastAPI()

@app.post("/users")
async def create_user(user: User):
    """
    
    """
    return user

@app.post("/multiple-objects")
async def multiple_objects(user: User, company:Company):
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/multiple-objects' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "user": {
        "name": "string",
        "age": 0
    },
    "company": {
        "name": "string"
    }
    }'
    """
    return {"user":user, "company":company}


@app.post("/users-priority")
async def users_priority(user: User, priority: int = Body(...,
ge=1, le=3)):
    return {"user": user, "priority": priority}