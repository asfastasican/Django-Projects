from fastapi import FastAPI
from typing import Optional

app=FastAPI()

@app.get("/items/{item_id}")
def index(item_id:int):
    return {"product_id":item_id}

@app.get("/items/{file_path:path}")
def index(file_path:str):
    return {"file_path":file_path}

@app.get("/query/")
def index(q:int=0,m:Optional[int]=10):
    return {"q":q,"m":m}
