#ALL
import numpy as np
import random
from time import sleep
def set_board(size=(10,10)):
    return np.full(size,"_")

#SETTING 3 BOARDS
my_board=set_board()
opp_hidden_board=set_board() #no print
opp_shots_board=set_board()

myboats = [] #arg of the funct
mylives=2 #same as nr of boat positions  #TRANSFER TO VARIABLES.PY
oppboats=[]
opplives=2


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
                continue

            if (random_row, random_column) in boatslist: #check if there's another boat in that position
                correct_coordinate = False
                continue
            #once it's passed every condition, we're sure it can append that coordinate
            random_boat.append((random_row, random_column))

        if correct_coordinate and len(random_boat) == boat_length:# if the coordinate is valid, update list of positions
            for position in random_boat:
                boatslist.append(position)
            break
    return random_boat

def place_boat(boat,board):
    for position in boat:
        board[position]="O"
    return board

#PLACING MY BOATS ON MY FINAL BOARD (main version)
my_board=place_boat(randomize_boat(4,myboats),my_board)
my_board=place_boat(randomize_boat(3,myboats),my_board)
my_board=place_boat(randomize_boat(3,myboats),my_board)
my_board=place_boat(randomize_boat(2,myboats),my_board)
my_board=place_boat(randomize_boat(2,myboats),my_board)
my_board=place_boat(randomize_boat(2,myboats),my_board)
my_board=place_boat(randomize_boat(1,myboats),my_board)
my_board=place_boat(randomize_boat(1,myboats),my_board)
my_board=place_boat(randomize_boat(1,myboats),my_board)
my_board=place_boat(randomize_boat(1,myboats),my_board)

#PLACING THE MACHINE'S BOATS (main version)
opp_hidden_board=place_boat(randomize_boat(4,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(3,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(3,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(2,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(2,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(2,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),opp_hidden_board)

print("PLAYER'S BOARD\n",my_board)

def player_shoots(opp_hidden_board, opp_shots_board, opplives): #choose lives from the adversary, not own
    while  opplives >0 and mylives >0:
        if mylives <1 or opplives <1:
            quit()
        sleep(1.0)
        print("Your turn! Opponent's lives:", opplives) #lives just for demo
        sleep(1.0)
        print("MACHINE'S POSITIONS SHOT\n",opp_shots_board)#, "\n Lives:",opplives)
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
        except UnboundLocalError:
            print("Enter a valid number between 0 and 9.")
            continue
        sleep(1.0)
        print("Shooting",position)      
        if opp_shots_board[position]=="~" or opp_shots_board[position]=="X": #check if the user already shot that position
            sleep(1.0)
            print("You already shot that position... Choose a different one.")
            continue
        if opp_hidden_board[position] == "_":
            sleep(1.0)
            print("You missed!")
            opp_hidden_board[position] = "~"
            opp_shots_board[position] = "~"
            sleep(1.0)
            print("MACHINE'S POSITIONS SHOT\n",opp_shots_board,"\n")
            return opp_shots_board #return gets you out of the function so that the turn finishes
        else:    
            sleep(1.5)
            opplives-=1 # decrease adversary's lives
            print("It's a hit! Opponent's lives:", opplives) #lives just for demo
            opp_shots_board[position] = "X"
            opp_hidden_board[position] = "X"
            sleep(1.0)
            if opplives>0:
                print("Keep playing and choose a new position!")
            elif mylives <1: #just in case
                sleep(1.5)
                print("You lost...")
                quit()
            elif opplives <1: 
                sleep(1.5)
                print("You won!")
                quit()
            
            sleep(1.5)
            #the user keeps shooting till they miss the shot
        #add if it's sunk: if boat[position] in boat: if "O" not in boat: sunk
#give option to quit()

#añadir print de vidas / barcos en pie
#DEFINIR TB PARA TURNO DE LA IA y hacer print de la coordenada
def machine_shoots(my_board, mylives):
    while mylives >0 and opplives >0:
        if mylives <1 or opplives <1:
            quit()
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
            return my_board #return exits the function so that the turn finishes
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
                print("You lost...")
                quit()
            elif opplives <1: #just in case
                sleep(1.5)
                print("You won!")
                quit()
            sleep(1.0)
#al acabar, print del tablero del oponente
#opción de quit o de restart?

def demoplay(opplives=2,mylives=2): #arg just to test, change variable later
    while mylives >0 and opplives >0:
        # if opplives<=0 or mylives<=0:
        #     quit()
        player_shoots(opp_hidden_board, opp_shots_board, opplives)
        # if opplives<=0 or mylives<=0:
        #     quit()
        machine_shoots(my_board, mylives)
    #     if opplives<=0 or mylives<=0:
    #         quit()
    # if mylives <1:
    #     sleep(1.0)
    #     print("You lost...")
    # elif opplives <1:
    #     sleep(1.0)
    #     print("You won!")

# machine_shoots(my_board, mylives)
demoplay()