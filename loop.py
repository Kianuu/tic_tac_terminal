

from main import Handler as g_hand

g_board = " | | \n" + "-----\n" + " | | \n" + "-----\n"+ " | | "


p1_board = [0, 0, 0,
            0, 0, 0,
            0, 0, 0,]

p2_board = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

victory = False
turn = 1

#                                   1 2 3
##                                  4 5 6
##                                  7 8 9

winning_boards = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def check_win(board):
    if board in winning_boards:
        return True
    


def game():
    while victory == False:
        print(g_board,"\n", "This is the state of the board ^^")
        if turn == 1:
            print(f"{g_hand.player_priority[min]} is X! It's their move. :)\n")
            change = int(input(g_board, + '\n' + f"Where will you play {g_hand.player_priority[min]}?"))
            match change:

                case 1:
                    g_board[0] = "X"
                    p1_board[0] = 1

                case 2:
                    g_board[2] = "X"
                    p1_board[1] = 2

                case 3:
                    g_board[4] = "X"
                    p1_board[2] = 3

                case 4:
                    g_board[10] = "X"
                    p1_board[3] = 4

                case 5:
                    g_board[12] = "X"
                    p1_board[4] = 5

                case 6:
                    g_board[14] = "X"
                    p1_board[5] = 6

                case 7:
                    g_board[20] = "X"
                    p1_board[6] = 7

                case 8:
                    g_board[22] = "X"
                    p1_board[7] = 8

                case 9:
                    g_board[24] = "X"
                    p1_board[8] = 9

            turn = 2
            if check_win(p1_board) == True:
                g_hand.player_scores[g_hand.name1] += 1
                print(g_board, "\n", f"{g_hand.name1} wins! The score is {g_hand.player_scores}")
                victory == True


            
        else: 
            print(f"{g_hand.player_priority[max]} is O! Now it's their move >:)\n")
            change = int(input(g_board, + '\n' + f"Where will you play {g_hand.player_priority[max]}?"))
            match change:

                case 1:
                    g_board[0] = "O"
                    p2_board[0] = 1

                case 2:
                    g_board[2] = "O"
                    p2_board[1] = 2

                case 3:
                    g_board[4] = "O"
                    p2_board[2] = 3

                case 4:
                    g_board[10] = "O"
                    p2_board[3] = 4

                case 5:
                    g_board[12] = "O"
                    p2_board[4] = 5

                case 6:
                    g_board[14] = "O"
                    p2_board[5] = 6

                case 7:
                    g_board[20] = "O"
                    p2_board[6] = 7

                case 8:
                    g_board[22] = "O"
                    p2_board[7] = 8

                case 9:
                    g_board[24] = "O"
                    p2_board[8] = 9

            turn = 1
        
            if check_win(p2_board) == True:
                g_hand.player_scores[g_hand.name2] += 1
                print(g_board, "\n", f"{g_hand.name2} wins! The score is {g_hand.player_scores}")
                victory == True



