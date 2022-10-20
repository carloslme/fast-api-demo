'''
In a REST API, query parameters are commonly used on read endpoints 
to apply pagination, a filter, a sorting order, or selecting fields.
'''
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/users")
async def get_user(page:int=1, size:int=10):
    """
    http://localhost:8000/users?page=5&size=50
    """
    return {"page":page, "size":size}
