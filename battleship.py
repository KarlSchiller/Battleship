from pandas import DataFrame
import numpy as np


class grid():
    '''Holds one battleship grid'''
    # TODO: explain attributes
    def __init__(self, player):
        self.game_over = False  # set to True if all ships are hit
        self.board = DataFrame(False,
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.shots = np.array([[False]*10]*10)    # shots taken
        self.player = player    # 'computer' or 'user'
        # TODO: add attribute that holds remaining ships
        # TODO: distribute ships on self.board

    def draw(self):
        '''Create a grid with printable characters'''
        print_grid = DataFrame(False,
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        if self.player == 'computer':
            print_grid[:] = ' ' # all non-shot water fields
            # element-wise multiplication of two boolean matrices, ~ inverts a matrix
            print_grid[np.multiply(~self.board,self.shots)] = '~' # all shot water fields
            print_grid[self.board] = '0' # all ships
            print_grid[np.multiply(self.board,self.shots)] = 'x' # all shot ship fields
        elif self.player == 'user':
            print_grid[:] = '?' # all non-shot fields
            print_grid[np.multiply(~self.board,self.shots)] = '~' # all shot water fields
            print_grid[np.multiply(self.board,self.shots)] = 'x' # all shot ship fields
        else:
            raise ValueError("grid player is neither 'user' nor 'computer'")
        return print_grid

    def __str__(self):
        '''Print grid in string format'''
        return self.draw().to_string(header=True, index=True)

    def shoot(self, row, col):
        '''Shoot at a field (row, col) and return ocean or hit'''
        # TODO: check, if field is already shot
        # TODO: Update shots
        # TODO: check, if a ship is hit
        # TODO: check if ship is destroyed
        # TODO: update ships attribute in case of destruction
        # TODO: check if game is over
        # TODO: return ocean, hit ,destroyal or game_over
        return "shoot result dummy text"


class Battleship():
    ''' The battleship game board '''
    # TODO: Explain attributes

    def __init__(self):
        # TODO: Initialise ship attribute of user and pc with param ships
        self.pc = grid('computer')
        self.user = grid('user')
        # number of ships. First index are ships of size one, second of size two etc.
        self.ships = [2,2,1,1,1]

    def __str__(self):
        pc = self.pc.draw()
        user = self.user.draw()
        indent = " "*2  # indent at the left side
        space = " "*8   # space between pc and user grid
        out = indent+"Computer"+" "*24+space+"User\n"
        out += indent+" "*4+"  ".join(pc.columns)+space+" "*4+"  ".join(user.columns)
        for row in range(len(pc)):
            out += "\n"+indent+"{:2d}  ".format(row+1)+"  ".join(pc.iloc[row,:])
            out += space+"{:2d}  ".format(row+1)+"  ".join(user.iloc[row,:])
        return out

    def distribute_ships(self):
        # TODO: Distribute ships
        pass

    def instructions(self):
        '''Print instructions of the battleship game'''
        # TODO
        # Basic introduction to game
        # Printed grids: what character means what?
        # Possible user inputs
        # How does the computer move?
        return "To be added."

    def create_computer_move(self):
        # TODO: let pc shoot randomly, except a ship is hit
        # return field string
        return "dummy field"

    def restart(self):
        # TODO: let the game restart (with new ship positions ^^)
        print("Restart game dummy text.")
        pass

    def remaining_ships(self):
        # TODO: print remaining ships of pc and user
        # return string to print
        return "Print ships dummy return string"
