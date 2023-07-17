


game_board = " | | \n" + "-----\n" + " | | \n" + "-----\n"+ " | | "
actual_board = [0, 0, 0,
                0, 0, 0,
                0, 0, 0,]

## to adjust line one values, gb[0], [2], [4], 
## to adjust line two values, gb[10]. [12], [14]
## to adjust line three values, gb[20], [22], [24]
## from top left to bottom right is :
#                                   1 2 3
##                                  4 5 6
##                                  7 8 9

game_state = True

main_menu = \
"Welcome to Tic Tac Terminal \n \n \n" + "**********  Press 1 for Single Player Mode  **********\n\n" + "**********  Press 2 for Multiplayer Player Mode  **********\n\n"

class handler(object):
    def __init__(self, name1, name2, player_scores, player_priority, gamemode):

        self.name1 = "Player 1"
        self.name2 = "Player 2"
        self.player_scores = {self.name1 : 0, self.name2 : 0}
        self.player_priority = {self.name1 : 1, self.name2 : 2}
        self.gamemode = 0

    def name_players(self):

        self.name1 = input(f"What is {self.name1}'s name? ")
        self.name2 = input(f"What about {self.name2}'s name? ")

    def print_scores(self):

        print(f"{self.name1} has {self.player_scores[self.name1]} wins, {self.name2} has {self.player_scores[self.name2]} wins. Keep it up! :)")

game_handler = handler(1, 1, 1, 1, 1)
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

    mode = input("Select your mode:  ")

    if mode == '1': 
       
       game_handler.name_players()
       print(game_handler.player_scores)
       play_state =  input(f"Welcome to Singleplayer! Your score is: {game_handler.player_scores}, would you like to play? ")

       if play_state == "no":
           ### Revisit, add return to main menu option
           print("Goodbye!")
           raise SystemExit()
       
       game_handler.gamemode = 1

       difficulty = int(input("please choose a difficulty: \n \
                              1: Easy \n \
                              2: Medium \n \
                              3: Impossible \n"))
       
       print("sorry, adding AI player later, try again soon!")
       continue

    elif mode == '2':

        game_handler.gamemode = 2
        ## Create main game loop and victory loop. Have it return the winner as 1 or 2 for player 1 and 2 and set up for reset 
        pass        

    else:

        exit_status = input("Sorry, would you like to exit or play? \n")

        if exit_status in ["exit", "Exit", "EXIT", "eXIT", "exIT", "exiT", "eXit", "exIt", "ExiT", "eXIt", "eXiT"]:

            print("Goodbye!")
            raise SystemExit()
        
        else:
            continue
    