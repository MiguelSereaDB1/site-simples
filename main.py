from fastapi import FastAPI
from pydantic import BaseModel

app: FastAPI = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
