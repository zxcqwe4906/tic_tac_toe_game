from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from game import Game, Player
from random_player import RandomPlayer
from ai_player import AIPlayer
from utils import get_turn_from_html_str, html_str_to_board

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def get_html(request: Request, board: Optional[str] = "000000000"):
    turn = get_turn_from_html_str(board)

    g = Game(Player(0), Player(1))
    g.board = html_str_to_board(board)
    is_end = g.is_end()

    if is_end == 1:
        end_text = "Circle Win !!"
    elif is_end == 2:
        end_text = "Cross Win !!"
    elif is_end == 3:
        end_text = "Draw"
    else:
        end_text = ""

    return templates.TemplateResponse(
        "tic_tac_toe.html",
        {
            "request": request,
            "board": board,
            "turn": turn,
            "is_end": is_end,
            "end_text": end_text,
        },
    )


@app.get("/ai")
def ai_move(request: Request, board: Optional[str] = "000000000"):
    # decide move
    turn = get_turn_from_html_str(board)
    p = AIPlayer(int(turn))
    move = p.generate_move(html_str_to_board(board))
    new_board = board[: move - 1] + turn + board[move:]

    # call / api
    return RedirectResponse(f"/?board={new_board}")
