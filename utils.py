def html_str_to_board(board_str: str):
    reutrn_board = []
    temp_list = []
    for c in board_str:
        temp_list.append(int(c))
        if len(temp_list) == 3:
            reutrn_board.append(temp_list)
            temp_list = []
    return reutrn_board

if __name__ == '__main__':
    print(html_str_to_board("122000211"))