from time import sleep
# import numpy as np
# import random
def intro_game():
    sleep(0.5)
    print("\t\t\t WELCOME TO BATTLESHIP!")
    sleep(1.0)
    print("\nHow to play:")
    print("\nThe aim of the game is to sink your opponent's ships before they sink yours!")
    sleep(1.5)
    print("\nIn this version, you will play against the machine. Your boats will be placed randomly across the board.")
    sleep(1.5)
    print("\nThen you will be prompted to enter a coordinate (row and column) between 0 and 9 to shoot your opponent's board, which you won't be able to see.")
    sleep(1.5)
    print("\nIf you hit a boat (represented as 'O'), an 'X' will be printed on the coordinate, whereas if you miss, a '~' will be printed.")
    sleep(1.5)
    print("\nLucky for you, when it's the machine's time to play, it will hit a random position in your board.")
    sleep(1.5)
    print("\nThe first one sinking all of the opponent's ships wins!")
    sleep(1.5)
    print("\nLET THE GAME BEGIN!")
    sleep(1.5)
    # mode=int(input("\nWhat kind of game do you want to play?\n1.Full version\n2.Short demo\n3.Quit\n(Enter a number)"))
    # while True:
    #     try:
    #         if mode==1:
    #             mylives=20 #same as total number of boats
    #             opplives=20
    #             playgame()
    #             break
    #         elif mode==2:
    #             mylives=3 #Demo: the first to achieve three hits
    #             opplives=3
    #             playgame()
    #             break
    #         elif mode==3:
    #             quit()
    #     except ValueError:
    #             print("Enter a number from 1 to 3.")
    #             continue
    
    

def player_shoots():
    global opplives
    while opplives >0:
        sleep(1.0)
        print("Your turn! Opponent's lives:", opplives) #lives just for demo
        sleep(1.0)
        print("MACHINE'S POSITIONS SHOT\n",opp_shots_board)
        sleep(1.0)
        print("(MACHINE'S HIDDEN BOARD) just for demo\n",opp_hidden_board) #NOT PRINTED IN MAIN GAME
        sleep(1.5)
        try:
            row=int(input("Enter a row between 0 and 9 to shoot."))
            if row < 0 or row > 9: #check if it is inside the board
                sleep(1.5)
                print("Enter a valid position.")
                continue # goes up to ask for new input
        except ValueError:
            sleep(1.0)
            print("Enter a valid number between 0 and 9.")
            continue

        try:
            column=int(input("Enter a column between 0 and 9 to shoot."))
            if column < 0 or column > 9: #check if it is inside the board
                sleep(1.0)
                print("Enter a valid position.")
                continue # goes up to ask for new input
        except ValueError:
            sleep(1.0)
            print("Enter a valid number between 0 and 9.")
            continue
        try:
            position=row,column
        except UnboundLocalError: #in case the input is empty
            print("Enter a valid number between 0 and 9.")
            continue
        sleep(1.0)
        print("Shooting",position)      
        if opp_shots_board[position]=="~" or opp_shots_board[position]=="X": #check if the user already shot that position
            sleep(1.0)
            print("You already shot that position... Choose a different one.")
            sleep(1.0)
            continue
        if opp_hidden_board[position] == "_":
            sleep(1.0)
            print("You missed!")
            opp_hidden_board[position] = "~"
            opp_shots_board[position] = "~"
            sleep(1.0)
            print("MACHINE'S POSITIONS SHOT\n",opp_shots_board,"\n")
            return opp_shots_board, opplives #return gets you out of the function so that the turn finishes
        else:    
            sleep(1.5)
            opplives-=1 # decrease adversary's lives
            print("It's a hit! Opponent's lives:", opplives) #lives just for demo
            opp_shots_board[position] = "X"
            opp_hidden_board[position] = "X"
            sleep(1.0)
            if opplives>0:
                print("Keep playing and choose a new position!")
            elif opplives <1: 
                sleep(1.5)
                print("You won!\nMACHINE'S HIDDEN BOARD\n")
                sleep(1.0)
                print(opp_hidden_board,"\n PLAYER'S BOARD\n",my_board)
                sleep(1.0)
                # choice=input("Do you want to play again? Y/n")        #to play again we would need to reset the board and the boats
                # if choice.lower()=="y":
                #     opplives=3
                #     continue
                # else:
                return opplives, quit()
            sleep(1.5)
            #the user keeps shooting till they miss the shot



def machine_shoots():
    global mylives
    while mylives >0:
        sleep(1.5)
        print("Machine's turn! Your lives:", mylives) #lives just for demo
        sleep(1.0)
        print("PLAYER'S BOARD\n",my_board)
        randrow = random.randint(0, 9)
        randcolumn = random.randint(0, 9)
        position=randrow,randcolumn
        sleep(2.0)
        print("Shooting",position)
        sleep(1.0)
        if my_board[position]=="~" or my_board[position]=="X": #check if the machine already shot that position
            continue
        if my_board[position] == "_":
            sleep(2.0)
            print("The machine missed!")
            my_board[position] = "~"
            sleep(1.0)
            print("PLAYER'S BOARD\n",my_board,"\n")
            return my_board, mylives #return exits the function so that the turn finishes
        else:    
            sleep(2.0)
            mylives-=1 # decrease player's lives
            print("It's a hit! Your lives:",mylives) #lives just for demo
            my_board[position] = "X"
            sleep(1.0)
            if mylives>0:
                print("The machine keeps playing!")
            elif mylives <1:
                sleep(1.5)
                print("You lost...\nMACHINE'S HIDDEN BOARD\n", opp_hidden_board, "\nPLAYER'S BOARD\n",my_board)
                sleep(1.0)
                # choice=input("Do you want to play again? Y/n")         #to play again we would need to reset the board and the boats
                # if choice.lower()=="y":
                #     mylives=3
                #     continue
                # else:
                return mylives, quit()
            sleep(1.0)

def playgame(): #couldn't set lives as args
    while mylives >0 and opplives >0:
        player_shoots()
        machine_shoots()