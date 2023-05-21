from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def get(request: Request, board: Optional[str] = "000000000"):
    count_dict = {'1': 0, '2': 0}
    for c in board:
        if c == '1':
            count_dict['1'] += 1
        elif c == '2':
            count_dict['2'] += 1

    if count_dict['1'] == count_dict['2']:
        turn = '1'
    elif count_dict['1'] - count_dict['2'] == 1:
        turn = '2'
    else:
        raise ValueError("board invalid")

    return templates.TemplateResponse(
        "tic_tac_toe.html",
        {
            "request": request,
            "board": board,
            "turn": turn,
        }
    )