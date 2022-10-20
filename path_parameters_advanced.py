from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{num1}/{num2}/{num3}/{num4}")
async def get_user(num1:int = Path(..., ge=1),
                    num2:int = Path(..., gt=1),
                    num3:int = Path(..., lt=1),
                    num4:int = Path(..., le=1)):
    return {"num1": num1, "num2": num2, "num3": num3, "num4": num4}

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path, min_lenght=3, max_lenght=5):
    return {"license":license}

@app.get("/license-plates-regex/{license}")
async def get_license_regex(license:str = 
                            Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")): #AB-123-CD (French license plates)
    return {"license":license}