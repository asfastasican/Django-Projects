from fastapi import FastAPI

app=FastAPI()

@app.get('/first')
def index():
    return "This is my first api project"
