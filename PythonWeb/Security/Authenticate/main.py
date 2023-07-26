from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    name: str

@app.post("/create/")
async def create(data: Data):
    return {"data": data}

@app.get("/teste/{item_id}")
async def test(item_id: str, query: int):
    return {"Hello": item_id}