from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "mundo melius quid fecisti"}

@app.get("/items/{item_id}")
def read_root(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}