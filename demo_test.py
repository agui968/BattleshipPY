import numpy as np
# import random
from battfunctions import *
import battvariables
#SETTING 3 BOARDS
# my_board=set_board()
# opp_hidden_board=set_board() #no print
# opp_shots_board=set_board()

myboats = [] #arg of the funct
# mylives=20 #same as nr of boat positions  #TRANSFER TO VARIABLES.PY
oppboats=[]
# opplives=20

#PLACING MY BOATS AND PRINTING MY FINAL BOARD (any my lives)
my_board=place_boat(randomize_boat(4,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(3,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(3,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(2,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(2,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(2,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(1,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(1,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(1,myboats),battvariables.my_board)
my_board=place_boat(randomize_boat(1,myboats),battvariables.my_board)
print("PLAYER'S BOARD\n",my_board, "\n Lives:",battvariables.mylives)
print(myboats)

#PLACING THE MACHINE'S BOATS
opp_hidden_board=place_boat(randomize_boat(4,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(3,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(3,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(2,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(2,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(2,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),battvariables.opp_hidden_board)
opp_hidden_board=place_boat(randomize_boat(1,oppboats),battvariables.opp_hidden_board)

print("MACHINE'S HIDDEN BOARD\n",battvariables.opp_hidden_board) #NOT PRINTED IN MAIN GAME

#PRINTING THE MACHINE'S BOARD WE'LL SEE AND SHOOT (and its lives)
print("MACHINE'S POSITIONS SHOT\n",battvariables.opp_shots_board, "\n Lives:",battvariables.opplives)

player_shoots()