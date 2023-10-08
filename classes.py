import numpy as np
import random
class Board:
    """
    Class to create a board to play Battleship. It also allows you to create random boats and place them in random positions on the board.
    """
    def __init__(self, size=(10,10)):
        """"Initiates the class and establishes the default size of the board."""
        self.size=size
        self.ships=[]

    def create_board(self):
        """
        Method to create an instance of the Board class. It's an empty 10x10 numpy array.
        """
        return np.full(self.size,"_")
    
    def randomize_boat(self,boat_length:int,ships:list):
        """
        Method that creates a random boat of a given length that will be added to a list of boats.
        """
        self.boat_length=boat_length
        self.ships=ships
        random_boat = []
        rdirection = random.choice(["N", "S", "E", "W"])
        while len(random_boat) < boat_length:
            random_row = random.randint(0, 9)
            random_column = random.randint(0, 9)
            random_boat = [(random_row, random_column)]

            correct_coordinate = True 
            #declare the variable so it keeps going through the loop till the bottom part (and the variable exists down there)
            for _ in range(1, boat_length):
                if rdirection == "W":
                    random_column -= 1
                elif rdirection == "E":
                    random_column += 1
                elif rdirection == "N":
                    random_row -= 1
                elif rdirection == "S":
                    random_row += 1

                if random_row < 0 or random_row > 9 or random_column < 0 or random_column > 9:
                    #check if it is inside the board
                    correct_coordinate = False
                    continue

                if (random_row, random_column) in self.ships:
                    #check if there's another boat in that position
                    correct_coordinate = False
                    continue
                #once it's passed every condition, we're sure the coordinate can be appended
                random_boat.append((random_row, random_column))

            if correct_coordinate and len(random_boat) == boat_length:# if the coordinate is valid, update list of ships
                for position in random_boat:
                    self.ships.append(position)
                break
        return random_boat


    def place_boat(self,boat,board):
            """
            Method that places the previously created boat on the board (given the coordinates of the previous method).
            """
            self.boat=boat
            self.board=board
            for position in self.boat:
                self.board[position]="O"
            return self.board

#CLASS INSTANCES
my_board_obj=Board()
opp_hidden_board_obj=Board() #not visible for player
opp_shots_board_obj=Board()

#CREATING 3 BOARDS
my_board=my_board_obj.create_board()
opp_hidden_board=opp_hidden_board_obj.create_board() #not visible for player
opp_shots_board=opp_hidden_board_obj.create_board()
