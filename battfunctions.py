import numpy as np
import random
import battvariables
import battobjects
 #CHANGE WHEN I DEFINE THE FINAL FILE

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
        try:
            row=int(input("Enter a row between 0 and 9 to shoot."))
            if row < 0 or row > 9: #check if it is inside the board
                print("Enter a valid position.")
                continue # goes up to ask for new input
        except ValueError:
            print("Enter a valid number between 0 and 9.")

        try:
            column=int(input("Enter a column between 0 and 9 to shoot."))
            if column < 0 or column > 9: #check if it is inside the board
                print("Enter a valid position.")
                continue # goes up to ask for new input
        except ValueError:
            print("Enter a valid number between 0 and 9.")
        
        position=row,column

        if battobjects.opp_shots_board[position]=="~" or battobjects.opp_shots_board[position]=="X": #check if the user already shot that position
            print("You already shot that position... Choose a different one.")
            continue

        if battobjects.opp_hidden_board[position] == "_":
            print("You missed!")
            battobjects.opp_hidden_board[position] = "~"
            battobjects.opp_shots_board[position] = "~"
            print(battobjects.opp_shots_board)
            return battobjects.opp_shots_board #return gets you out of the function so that the turn finishes
        else:    
            print("It's a hit!")
            battobjects.opp_shots_board[position] = "X"
            battobjects.opp_hidden_board[position] = "X"
            battvariables.opplives-=1 # decrease adversary's lives
            print(battobjects.opp_shots_board) #CHECK IF THAT WORKS
            print("Keep playing and choose a new position!")
            #the user keeps shooting till they miss the shot

        #add if it's sunk: if boat[position] in boat: if "O" not in boat: sunk
#give option to quit()

#añadir print de vidas / barcos en pie
#DEFINIR TB PARA TURNO DE LA IA y hacer print de la coordenada

#al acabar, print del tablero del oponente
#opción de quit o de restart?

def machine_shoots():
    while True:
        randrow = random.randint(0, 9)
        randcolumn = random.randint(0, 9)
        position=randrow,randcolumn

        if battobjects.my_board[position]=="~" or battobjects.my_board[position]=="X": #check if the machine already shot that position
            continue
        if battobjects.my_board[position] == "_":
            print("The machine missed!")
            battobjects.my_board[position] = "~"
            print(battobjects.my_board)
            return battobjects.my_board #return exits the function so that the turn finishes
        else:    
            print("It's a hit!")
            battobjects.my_board[position] = "X"
            battvariables.mylives-=1 # decrease player's lives
            print(battobjects.my_board) #CHECK IF THAT WORKS
            print("The machine keeps playing!")