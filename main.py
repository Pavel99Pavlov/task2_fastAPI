from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Павлов Павел Дмитриевич"}

@app.get('/tools')
async def f_indexT():
    return "навыки плохие"

@app.get('/users')
async def f_indexU():
    return "+79609429936"