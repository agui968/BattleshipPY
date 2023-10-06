#VARIABLES
import numpy as np
import battfunctions

#SETTING 3 BOARDS
my_board=battfunctions.set_board()
opp_hidden_board=battfunctions.set_board() #no print
opp_shots_board=battfunctions.set_board()
# print(my_board)
myboats = [] #arg of the funct
mylives=20 #same as nr of boat positions  #TRANSFER TO VARIABLES.PY
oppboats=[]
opplives=20
board_size=(10,10)