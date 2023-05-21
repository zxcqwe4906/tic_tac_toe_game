def get_turn_from_html_str(board_str: str) -> str:
    count_dict = {"1": 0, "2": 0}
    for c in board_str:
        if c == "1":
            count_dict["1"] += 1
        elif c == "2":
            count_dict["2"] += 1

    if count_dict["1"] == count_dict["2"]:
        return "1"
    elif count_dict["1"] - count_dict["2"] == 1:
        return "2"
    else:
        raise ValueError("board invalid")


def html_str_to_board(board_str: str):
    reutrn_board = []
    temp_list = []
    for c in board_str:
        temp_list.append(int(c))
        if len(temp_list) == 3:
            reutrn_board.append(temp_list)
            temp_list = []
    return reutrn_board


if __name__ == "__main__":
    print(html_str_to_board("122000211"))
