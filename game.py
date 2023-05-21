"""
A tic tac toe game:
|1|2|3|
|4|5|6|
|7|8|9|

###########################
Design of board:
0: empty
1: O
2: X
"""

class Player:
    """Player Class
    generate_move: play a move based on board
    """
    def __init__(self, turn: int) -> None:
        self.turn = turn

    def generate_move(self, board) -> int:
        num = input("enter a move: ")
        return int(num)


class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.check_moves = [
            [1, 0],
            [0, 1],
            [1, 1],
            [-1, 1],
        ]
        self.player1 = player1
        self.player2 = player2

        if self.player1.turn == 1:
            self.current_player = player1
        else:
            self.current_player = player2
        self.hint_str = """
        |1|2|3|
        |4|5|6|
        |7|8|9|
        """

    def print_board(self):
        for row in self.board:
            row_str = '|'
            for num in row:
                if num == 0:
                    row_str = row_str + ' |'
                elif num == 1:
                    row_str = row_str + 'O|'
                elif num == 2:
                    row_str = row_str + 'X|'
            print(row_str)

    def change_player(self) -> int:
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play_move(self, print_board=False):
        position_num = self.current_player.generate_move(self.board) - 1
        self.board[position_num // 3][position_num % 3] = self.current_player.turn
        if print_board:
            self.print_board()
            print('--------------------------------')
        self.change_player()

    def check_consecutive(self, i, j):
        for move in self.check_moves:
            all_one = True
            all_two = True
            for x in range(3):
                new_x = i + x * move[0]
                new_y = j + x * move[1]
                if new_x >= 3 or new_y >= 3 or new_x < 0 or new_y < 0:
                    all_one = False
                    all_two = False
                    break

                if self.board[new_x][new_y] != 1:
                    all_one = False
                if self.board[new_x][new_y] != 2:
                    all_two = False

            if all_one == True:
                return 1
            elif all_two == True:
                return 2

        return 0

    def is_end(self):
        is_full = True
        for i, row in enumerate(self.board):
            for j, _ in enumerate(row):
                if self.board[i][j] == 0:
                    is_full = False
                result = self.check_consecutive(i, j)
                if result == 1:
                    return 1
                elif result == 2:
                    return 2
        if is_full:
            return 3
        return 0

