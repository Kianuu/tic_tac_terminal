## Holds code I don't want to lose 


winning_boards = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

test_board = [1, 0, 3,
              0, 5, 0,
              0, 0, 9]

p1_board = [1, 0, 0,
            4, 0, 0,
            7, 0, 0,]

p2_board = [1, 0, 0,
            0, 5, 0,
            0, 0, 9]

def check_win(board, win_cond):
    combo = []
    for i in win_cond:
        combo = [board[i[0] - 1], board[i[1] - 1], board[i[2] - 1]]
        if combo == i:
            return True
    return False




if check_win(test_board, winning_boards) == True:
    print("It worked")
else:
    print("It did not work")


if check_win(p2_board, winning_boards) == True:
    print("It worked")
else:
    print("It did not work")