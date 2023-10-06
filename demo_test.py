import numpy as np
# import random
import battfunctions
import battvariables
#SETTING 3 BOARDS
my_board=battfunctions.set_board()
opp_hidden_board=battfunctions.set_board() #no print
opp_shots_board=battfunctions.set_board()

myboats = [] #arg of the funct
# mylives=20 #same as nr of boat positions  #TRANSFER TO VARIABLES.PY
oppboats=[]
# opplives=20

#PLACING MY BOATS AND PRINTING MY FINAL BOARD (any my lives)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(4,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(3,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(3,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(2,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(2,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(2,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,myboats),my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,myboats),my_board)
print("PLAYER'S BOARD\n",my_board, "\n Lives:",battvariables.mylives)
print(myboats)

#PLACING THE MACHINE'S BOATS
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(4,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(3,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(3,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(2,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(2,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(2,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,oppboats),opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,oppboats),opp_hidden_board)

print("MACHINE'S HIDDEN BOARD\n",opp_hidden_board) #NOT PRINTED IN MAIN GAME

#PRINTING THE MACHINE'S BOARD WE'LL SEE AND SHOOT (and its lives)
print("MACHINE'S POSITIONS SHOT\n",opp_shots_board, "\n Lives:",battvariables.opplives)

battfunctions.player_shoots()