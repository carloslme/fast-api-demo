from fastapi import FastAPI

app = FastAPI()

# In Python, a decorator is syntactic sugar that allows you to wrap a
#  function or class with common logic without compromising readability.
#  It's roughly equivalent to app.get("/")(hello_world).
@app.get("/")
async def hello_world():
    return {"hello": "world"}