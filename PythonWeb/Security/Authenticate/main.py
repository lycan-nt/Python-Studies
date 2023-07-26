from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

@app.get("/teste/{item_id}")
async def test(item_id: str, query: int):
    return {"Hello": item_id}