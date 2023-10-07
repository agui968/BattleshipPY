import numpy as np
# import random
import battfunctions
import battvariables
import battobjects
#SETTING 3 BOARDS
# my_board=battfunctions.set_board()
# opp_hidden_board=battfunctions.set_board() #no print
# opp_shots_board=battfunctions.set_board()

# myboats = [] #arg of the funct
# # mylives=20 #same as nr of boat positions  #TRANSFER TO VARIABLES.PY
# oppboats=[]
# # opplives=20

#PLACING MY BOATS AND PRINTING MY FINAL BOARD (any my lives)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(4,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(3,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(3,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(2,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(2,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(2,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.myboats),battobjects.my_board)
my_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.myboats),battobjects.my_board)
print("PLAYER'S BOARD\n",my_board, "\n Lives:",battvariables.mylives)
print(battobjects.myboats)

#PLACING THE MACHINE'S BOATS
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(4,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(3,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(3,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(2,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(2,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(2,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.oppboats),battobjects.opp_hidden_board)
opp_hidden_board=battfunctions.place_boat(battfunctions.randomize_boat(1,battobjects.oppboats),battobjects.opp_hidden_board)

print("MACHINE'S HIDDEN BOARD\n",battobjects.opp_hidden_board) #NOT PRINTED IN MAIN GAME

#PRINTING THE MACHINE'S BOARD WE'LL SEE AND SHOOT (and its lives)
print("MACHINE'S POSITIONS SHOT\n",battobjects.opp_shots_board, "\n Lives:",battvariables.opplives)

battfunctions.player_shoots()