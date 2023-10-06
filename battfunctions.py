import numpy as np
import random
import battvariables
from demo_test import * #CHANGE WHEN I DEFINE THE FINAL FILE

def set_board(size=(10,10)):
    return np.full(size,"_")

def randomize_boat(boat_length:int,boatslist:list):
    random_boat = []
    #in or outside the funct?
    while len(random_boat) < boat_length:
        rdirection = random.choice(["N", "S", "E", "W"])

        random_row = random.randint(0, 9)
        random_column = random.randint(0, 9)
        random_boat = [(random_row, random_column)]

        correct_coordinate = True  #so it keeps going through the loop till the bottom part

        for _ in range(1, boat_length):
            if rdirection == "W":
                random_column -= 1
            elif rdirection == "E":
                random_column += 1
            elif rdirection == "N":
                random_row -= 1
            elif rdirection == "S":
                random_row += 1

            if random_row < 0 or random_row > 9 or random_column < 0 or random_column > 9: #check if it is inside the board
                correct_coordinate = False
                break

            if (random_row, random_column) in boatslist: #check if there's another boat in that position
                correct_coordinate = False
                break
            #once it's passed every condition, we're sure it can append that coordinate
            random_boat.append((random_row, random_column))

        if correct_coordinate:# if the coordinate is valid, update list of positions
            for position in random_boat:
                boatslist.append(position)
            break
    return random_boat

def place_boat(boat,board):
    for position in boat:
        board[position]="O"
    return board

def player_shoots(): #choose lives from the adversary, not own
    
    while True:
        row=int(input("Enter a row between 0 and 9 to shoot."))
        column=int(input("Enter a column between 0 and 9 to shoot."))
        position=row,column
        if row < 0 or row > 9 or column < 0 or column > 9: #check if it is inside the board
            print("Enter a valid position.")
            continue # goes up to ask for new input
        elif demo_test.opp_shots_board[position]=="~" or demo_test.opp_shots_board[position]=="X": #check if the user already shot that position
            print("You already shot that position... Choose a different one.")
            continue

        if demo_test.opp_hidden_board[position] == "_":
            print("You missed!")
            demo_test.opp_hidden_board[position] = "~"
            demo_test.opp_shots_board[position] = "~"
            print(demo_test.opp_shots_board)
            return demo_test.opp_shots_board #return gets you out of the function so that the turn finishes
        else:    
            print("It's a hit!")
            demo_test.opp_shots_board[position] = "X"
            demo_test.opp_hidden_board[position] = "X"
            lives-=1 # decrease adversary's lives
            print(demo_test.opp_shots_board) #CHECK IF THAT WORKS
            print("Keep playing and choose a new position!")
            #the user keeps shooting till they miss the shot

        #add if it's sunk: if boat[position] in boat: if "O" not in boat: sunk
#give option to quit()

#añadir print de vidas / barcos en pie
#DEFINIR TB PARA TURNO DE LA IA y hacer print de la coordenada

#al acabar, print del tablero del oponente
#opción de quit o de restart?