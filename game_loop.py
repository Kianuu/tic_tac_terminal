

from tic_tac_terminal.main import game_board as g_board
from tic_tac_terminal.main import game_handler as g_hand


victory = False
turn = 1


def check_win():
    pass ## work on this later



while victory == False:
    print(g_board,"\n", "This is the state of the board ^^")
    if turn == 1:
        print(f"{g_hand.player_priority[min]} is X! It's their move. :)\n")
        change = int(input(g_board, + '\n' + f"Where will you play {g_hand.player_priority[min]}?"))
        match change:
            case 1:
                g_board[0] = "X"
            case 2:
                g_board[2] = "X"
            case 3:
                g_board[4] = "X"
            case 4:
                g_board[10] = "X"
            case 5:
                g_board[12] = "X"
            case 6:
                g_board[14] = "X"
            case 7:
                g_board[20] = "X"
            case 8:
                g_board[22] = "X"
            case 9:
                g_board[24] = "X"
        turn = 2
        
    else: 
        print(f"{g_hand.player_priority[max]} is O! Now it's their move >:)\n")
        change = int(input(g_board, + '\n' + f"Where will you play {g_hand.player_priority[max]}?"))
        match change:
            case 1:
                g_board[0] = "O"
            case 2:
                g_board[2] = "O"
            case 3:
                g_board[4] = "O"
            case 4:
                g_board[10] = "O"
            case 5:
                g_board[12] = "O"
            case 6:
                g_board[14] = "O"
            case 7:
                g_board[20] = "O"
            case 8:
                g_board[22] = "O"
            case 9:
                g_board[24] = "O"
        turn = 1
    
    check_win()


