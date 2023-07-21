
g_board = " | | \n" + "-----\n" + " | | \n" + "-----\n" + " | | \n" 


p1_board = [0, 0, 0,
            0, 0, 0,
            0, 0, 0,]

p2_board = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

victory = False


#                                   1 2 3
##                                  4 5 6
##                                  7 8 9

winning_boards = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def check_win(board):
    if board in winning_boards:
        return True
    


def game():
    turn = 1
    while victory == False:
        print(g_board,"\n", "This is the state of the board ^^")
        if turn == 1:
            print(f"{game_handler.name1} is X! It's their move. :)\n")
            change = int(input(g_board + '\n' + f"Where will you play {game_handler.name1}? "))
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
                game_handler.player_scores[game_handler.name1] += 1
                print(g_board, "\n", f"{game_handler.name1} wins! The score is {game_handler.player_scores}")
                victory == True


            
        else: 
            print(f"{game_handler.name2} is O! Now it's their move >:)\n")
            change = int(input(g_board, +  f"Where will you play {game_handler.name2}?"))
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
                game_handler.player_scores[game_handler.name2] += 1
                print(g_board, "\n", f"{game_handler.name2} wins! The score is {game_handler.player_scores}")
                victory == True




## to adjust line one values, gb[0], [2], [4], 
## to adjust line two values, gb[10]. [12], [14]
## to adjust line three values, gb[20], [22], [24]
## from top left to bottom right is :
#                                   1 2 3
##                                  4 5 6
##                                  7 8 9

game_state = True

main_menu = \
            "Welcome to Tic Tac Terminal \n \n \n" + "**********  Press 1 for Single Player Mode  **********\n\n" \
            + "**********  Press 2 for Multiplayer Player Mode  **********\n\n"

class Handler(object):

    def __init__(self, name1, name2, player_scores, player_priority, gamemode):

        self.name1 = "Player 1"
        self.name2 = "Player 2"
        self.player_scores = {self.name1 : 0, self.name2 : 0}
        self.player_priority = {self.name1 : 1, self.name2 : 2}
        self.gamemode = 0


## sets player names, adjusts player_scores values 
    def name_players(self, game_mode):

        if game_mode == '2':

            self.name1 = input(f"What is {self.name1}'s name? ")
            self.name2 = input(f"What about {self.name2}'s name? ")
            self.player_scores = {self.name1: 0, self.name2: 0}

        else:

            self.name = input(f"What is {self.name1}'s name? ")


    def print_scores(self):

        print(f"{self.name1} has {self.player_scores[self.name1]} wins, {self.name2} has {self.player_scores[self.name2]} wins. Keep it up! :)")

game_handler = Handler(1, 1, 1, 1, 1)
#print(game_handler.name1)
#print(game_handler.player_priority)
#print(game_handler.player_scores)
#print(game_handler.gamemode)


while game_state == True:
    print(main_menu)
    

    print("Would you like to player singleplayer (1) or multiplayer (2)?\n\n")

    ## Add help and settings menu, help to see what other commands like score, view player names, view match history / view match replay. later.
    ## For settings, allow things like customized victory messages, profiles and passwords, ability to delete profiles, change password, delete
    ## match history etc, help should also explain the rules.

    game_handler.gamemode = input("Select your mode:  ")

    if game_handler.gamemode == '1': 
       
       game_handler.name_players()
       play_state =  input(f"Welcome to Singleplayer! You have {game_handler.player_scores[game_handler.name1]} wins, would you like to play? (yes or no): ")

       if play_state.lower() == "no":
           
           ### Revisit, add return to main menu option
           return_main = input("Would you like to return to the main menu? (yes or no): ")
           if return_main.lower() == "yes":
               continue
           else:
               print("Goodbye!")
               raise SystemExit()
       elif play_state.lower() == "yes":

            difficulty = int(input("please choose a difficulty: \n \
                                    1: Easy \n \
                                    2: Medium \n \
                                    3: Impossible \n"))
       
            print("sorry, adding AI player later, try again soon!")
            continue

    elif game_handler.gamemode == '2':

        game_handler.name_players(game_handler.gamemode)
        print(game_handler.name1, game_handler.name2)
        play_state =  input(f"Welcome to Multiplayer! {game_handler.name1} has {game_handler.player_scores[game_handler.name1]} wins, {game_handler.name2} has {game_handler.player_scores[game_handler.name2]} wins, would you like to play? (yes or no): ")

        if play_state.lower() == "no":

            return_main = input("Would you like to return to the main menu? (yes or no): ")
            if return_main.lower() == "yes":
                continue
            else:
                print("Goodbye!")
                raise SystemExit()
            
        elif play_state.lower() == "yes":
            game()
            


    else:

        exit_status = input("Would you like to exit? (yes or no) \n")

        if exit_status.lower() == "yes":
            print("Goodbye!")
            raise SystemExit()
        
        else:
            continue
    


