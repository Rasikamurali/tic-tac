import math 
import random 

class Player: 
    def __init__(self, letter): 
        #letter o or x 
        self.letter = letter 

    #we want all player to get their next moce given a game 
    def get_move(self, game): 
        pass 

class RandomComputerPLayer(Player): 
    def __init__(self, letter): 
        super().__init__(letter)
    def get_move(self, game): 
        square = random.choice(game.available_moves())
        return square 

class HumanPlayer(Player): 
    def __init__(self, letter): 
        super().__init__(letter)

    def get_move(self, game): 
        valid_square = False 
        val = None 
        while not valid_square: 
            square = input(self.letter + '\'s turn, input move (0-9):' )
            # checking if correct value is being cast to an integer 
            # if not, then invalid 
            # if that spot is not available, then we also say invalid 
            try: 
                val = int(square)
                if val not in game.available_moves(): 
                    raise ValueError 
                valid_square= True 
            except ValueError: 
                print('Invalid square. Try again')

        return val 