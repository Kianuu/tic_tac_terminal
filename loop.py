








def check_win(board, win_cond):
    combo = []
    for i in win_cond:
        combo = [board[i[0] - 1], board[i[1] - 1], board[i[2] - 1]]
        if combo == i:
            return True
    return False
    
def game(player1, player2, score, g_board, p1_board, p2_board, victory, turn, win_cond, mutable_board):
    turn = 1
    while victory == False:
        print(g_board,"\n", "This is the state of the board ^^")
        if turn == 1 and victory == False:
            print(f"{player1} is X! It's their move. :)\n")
            change = int(input(f" Where will you play {player1}? "))
            match change:

                case 1:
                    mutable_board[0] = 'X'
                    p1_board[0] = 1
                    g_board = ''.join(map(str, mutable_board))
                    

                case 2:
                    mutable_board[2] = "X"
                    p1_board[1] = 2
                    g_board = ''.join(map(str, mutable_board))                    

                case 3:
                    mutable_board[4] = "X"
                    p1_board[2] = 3
                    g_board = ''.join(map(str, mutable_board))

                case 4:
                    mutable_board[12] = "X"
                    p1_board[3] = 4
                    g_board = ''.join(map(str, mutable_board))

                case 5:
                    mutable_board[14] = "X"
                    p1_board[4] = 5
                    g_board = ''.join(map(str, mutable_board))

                case 6:
                    mutable_board[16] = "X"
                    p1_board[5] = 6
                    g_board = ''.join(map(str, mutable_board))

                case 7:
                    mutable_board[24] = "X"
                    p1_board[6] = 7
                    g_board = ''.join(map(str, mutable_board))

                case 8:
                    mutable_board[26] = "X"
                    p1_board[7] = 8
                    g_board = ''.join(map(str, mutable_board))

                case 9:
                    mutable_board[28] = "X"
                    p1_board[8] = 9
                    g_board = ''.join(map(str, mutable_board))

            turn = 2
            victory = check_win(p1_board, win_cond)
            if victory == True:
                score[player1] += 1
                print(f"{player1} wins! The score is {score}")
    
            
 
        if turn == 2 and victory == False:
            print(g_board,"\n", "This is the state of the board ^^\n")
            print(f"{player2} is O! Now it's their move >:)\n")
            change = int(input(f" Where will you play {player2}?"))
            match change:

                case 1:
                    mutable_board[0] = "O"
                    p2_board[0] = 1
                    g_board = ''.join(map(str, mutable_board))

                case 2:
                    mutable_board[2] = "O"
                    p2_board[1] = 2
                    g_board = ''.join(map(str, mutable_board))

                case 3:
                    mutable_board[4] = "O"
                    p2_board[2] = 3
                    g_board = ''.join(map(str, mutable_board))

                case 4:
                    mutable_board[12] = "O"
                    p2_board[3] = 4
                    g_board = ''.join(map(str, mutable_board))

                case 5:
                    mutable_board[14] = "O"
                    p2_board[4] = 5
                    g_board = ''.join(map(str, mutable_board))

                case 6:
                    mutable_board[16] = "O"
                    p2_board[5] = 6
                    g_board = ''.join(map(str, mutable_board))

                case 7:
                    mutable_board[24] = "O"
                    p2_board[6] = 7
                    g_board = ''.join(map(str, mutable_board))

                case 8:
                    mutable_board[26] = "O"
                    p2_board[7] = 8
                    g_board = ''.join(map(str, mutable_board))

                case 9:
                    mutable_board[28] = "O"
                    p2_board[8] = 9
                    g_board = ''.join(map(str, mutable_board))

            turn = 1
            victory = check_win(p2_board, win_cond)
            if victory == True:
                score[player2] += 1
                print(f"{player2} wins! The score is {score}")

