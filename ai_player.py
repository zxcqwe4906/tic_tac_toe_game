from copy import deepcopy
from game import Game
from random_player import RandomPlayer

class AIPlayer:
    def __init__(self, turn: int) -> None:
        self.turn = turn

    def get_legal_moves(self, board) -> list:
        return_list = []
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == 0:
                    return_list.append(i * 3 + j + 1)
        return return_list

    def simulate(self, board: list, num=1) -> tuple:
        """
        Returns (self turn win, self turn loss, draw)
        """
        d = {1: 0, 2: 0, 3: 0}
        for _ in range(num):
            new_board = deepcopy(board)

            game = Game(RandomPlayer(1), RandomPlayer(2))
            game.board = new_board

            if self.turn == 1:
                game.change_player()

            while True:
                is_end = game.is_end()
                if is_end:
                    break
                game.play_move()
            d[is_end] += 1

        if self.turn == 1:
            return (d[1], d[2], d[3])
        else:
            return (d[2], d[1], d[3])

    def generate_move(self, board) -> int:
        legal_moves = self.get_legal_moves(board)
        print('legal_moves:', legal_moves)
        num = 1000
        best_score = -num
        best_move = None
        for legal_move in legal_moves:
            x = (legal_move - 1) // 3
            y = (legal_move - 1) % 3
            board[x][y] = self.turn
            win, loss, draw = self.simulate(board, num=num)
            score = win - loss + 0.7 * draw
            if score > best_score:
                best_score = score
                best_move = legal_move
            board[x][y] = 0
        return best_move

if __name__ == "__main__":
    board = [[1, 2, 0], [0, 0, 0], [0, 0, 0]]
    player = AIPlayer(1)
    # print(player.simulate(board, num=1000))
    print(player.generate_move(board))