from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from game import Game, Player
from utils import html_str_to_board

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

    g = Game(Player(0), Player(1))
    g.board = html_str_to_board(board)
    is_end = g.is_end()

    print(f'is_end: {is_end}')
    if is_end == 1:
        end_text = 'Circle Win !!'
    elif is_end == 2:
        end_text = 'Cross Win !!'
    elif is_end == 3:
        end_text = 'Draw'
    else:
        end_text = ''

    return templates.TemplateResponse(
        "tic_tac_toe.html",
        {
            "request": request,
            "board": board,
            "turn": turn,
            "is_end": is_end,
            "end_text": end_text
        }
    )