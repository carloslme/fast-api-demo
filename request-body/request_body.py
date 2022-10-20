"""The body is the part of the HTTP request that contains raw data, 
representing documents, files, or form submissions. In a REST API, 
it's usually encoded in JSON and used to create structured objects in a database.

For the simplest cases, retrieving data from the body works exactly like query parameters. 
The only difference is that you always have to use the Body function; otherwise, 
FastAPI will look for it inside the query parameters by default.
"""
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/users")
async def create_user(name: str = Body(...),
                      age: int = Body(...)): # (...) means that the argument is required
    """
    curl -X 'POST' \
        'http://127.0.0.1:8000/users' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "name": "sdfs",
        "age": "2"
        }'
    
    """
    return {"name":name, "age":age}

