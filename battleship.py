from pandas import DataFrame
import numpy as np
# TODO: only import needed parts of numpy
from random import sample





class _Grid():
    '''Holds one battleship Grid'''
    # TODO: explain attributes
    def __init__(self, player, ship_nmbrs):
        self.game_over = False  # set to True if all ships are hit
        self.board = DataFrame(0,   # distribution of ships
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.shots = DataFrame(False,   # shots taken
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.player = player    # 'computer' or 'user'
        self.ship_nmbrs = ship_nmbrs # array with ship distribution

    def __str__(self):
        '''Print grid in string format'''
        return self.draw().to_string(header=True, index=True)

    def draw(self):
        '''Create a grid with printable characters'''
        print_grid = DataFrame('dummy',
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        if self.player == 'computer':
            print_grid[:] = ' ' # all non-shot water fields
            # element-wise multiplication of two boolean matrices, board==0 is a boolean mask
            print_grid[np.multiply(self.board==0,self.shots)] = '~' # all shot water fields
            print_grid[self.board!=0] = '0' # all ships
            print_grid[np.multiply(self.board!=0,self.shots)] = 'x' # all shot ship fields
        elif self.player == 'user':
            pass
            print_grid[:] = '?' # all non-shot fields
            print_grid[np.multiply(self.board==0,self.shots)] = '~' # all shot water fields
            print_grid[np.multiply(self.board!=0,self.shots)] = 'x' # all shot ship fields
        else:
            raise ValueError("grid player is neither 'user' nor 'computer'")
        return print_grid

    def shoot(self, shoot_str):
        '''Shoot at a field (row, col) and return ocean or hit'''
        # row in 'A', 'B', ... Replace with 0, 1, ... by getting ASCII number
        col = shoot_str[0]
        row = int(shoot_str[1:])
        if self.shots[col][row] == True:
            return 'Field is already shot'
        self.shots[col][row] = True    # Save shot

        if self.board[col][row] != 0:   # check, if a ship is hit
            if self._is_destroyed(col, row): # check, if it is destroyed
                ship_size = self._get_ship_size(col, row)
                # update ship_nmbrs attribute
                # convert index 0...4 to ship size 1...5 by index=|ship_size - 5|
                if self.ship_nmbrs[abs(ship_size-5)] <= 0:
                    raise ValueError("ship number array counts no ships of this size.")
                else:
                    self.ship_nmbrs[abs(ship_size-5)] -= 1
                if self.ship_nmbrs.sum() == 0: # are there ships left?
                    self.game_over = True
                return 'Destroyal'
            return 'Hit'
        return "Ocean"

    def _get_ship_size(self, col, row):
        '''Gives ship sizes of a ship at (col, row)'''
        # self.board[col][row] gets number of ship on the board
        # Firstly, mask all fields that contain the ship
        # Secondly, get a flattened numpy array of True's and False's
        # Lastly, sum up the array. True is counted as 1, False as 0
        return np.sum((self.board==self.board[col][row]).values.flatten())

    def _is_destroyed(self, col, row):
        '''Checks if ship is destroyed
        col, row represent a field on the board, where a part of the ship is located'''
        # self.board[col][row] gets number of ship on the board
        # Firstly, mask all fields that contain the ship.
        # Secondly, get shot values of these fields
        # Lastly, check with np.all if they are all shot (True)
        return np.all(self.shots[self.board == self.board[col][row]])

    def distribute_ships(self):
        '''Distribute ships on grid'''
        # #(rows) = #(cols) -> only use one axis to randomly pick fields
        axis = range(len(self.board.index))
        direction = ['left', 'right', 'up', 'down']
        # TODO: Smarter way than placing ships at random positions
        counter = 1 # shipnumber to distinguish ships
        for ship_type, shipnum in enumerate(self.ship_nmbrs): # for every ship size, start with largest ship
            for ship in range(shipnum):   # for every ship of type ship_type
                ship_placed = False
                while not ship_placed:
                    rndm_field = sample(axis, 2)    # random row and col number
                    rndm_direction = sample(direction, 1)[0]    # random direction
                    ship_placed = self._place_ship(rndm_field, rndm_direction, 5-ship_type, counter)
                counter += 1 # next ship
        #  print("Needed {} iterations (out of {} at minimum)".format(cntr_temp, self.ship_nmbrs.sum()))

    def _place_ship(self, field, direction, ship_len, counter):
        ''' Help function for distribute_ships method

        Checks if a ship of length @ship_len can be placed in direction @direction,
        starting from field @field.
        Places the ship and returns True, if that is possible'''
        max_len = len(self.board.index) # outer range of board
        if direction == 'left':
            if (field[1]+1-ship_len < 0):
                return False    # index beyond grid boundary
            if np.all(self.board.iloc[field[0], (field[1]+1-ship_len):(field[1]+1)] == 0):
                self.board.iloc[field[0], (field[1]+1-ship_len):(field[1]+1)] = counter
                return True     # ship placed
            else:
                return False    # another ship is alreay located here
        elif direction == 'right':
            if (field[1]+ship_len > max_len):
                return False    # index beyond grid boundary
            if np.all(self.board.iloc[field[0], field[1]:(field[1]+ship_len)] == 0):
                self.board.iloc[field[0], field[1]:(field[1]+ship_len)] = counter
                return True     # ship placed
            else:
                return False    # another ship is alreay located here
        elif direction == 'up':
            if (field[0]+1-ship_len < 0):
                return False    # index beyond grid boundary
            if np.all(self.board.iloc[(field[0]+1-ship_len):(field[0]+1), field[1]] == 0):
                self.board.iloc[(field[0]+1-ship_len):(field[0]+1), field[1]] = counter
                return True     # ship placed
            else:
                return False    # another ship is alreay located here
        elif direction == 'down':
            if (field[0]+ship_len > max_len):
                return False    # index beyond grid boundary
            if np.all(self.board.iloc[field[0]:(field[0]+ship_len), field[1]] == 0):
                self.board.iloc[field[0]:(field[0]+ship_len), field[1]] = counter
                return True     # ship placed
            else:
                return False    # another ship is alreay located here
        else:   # something went wrong
            raise ValueError("Ship direction not in 'left', 'right', 'up' or 'down'")
            return False


class Battleship():
    ''' The battleship game board '''
    # TODO: Explain attributes

    def __init__(self):
        # number of ships. First index are ships of size one, second of size two etc.
        self.ship_nmbrs = []
        self.pc = _Grid('computer', self.ship_nmbrs)
        self.user = _Grid('user', self.ship_nmbrs)

    def __str__(self):
        pc = self.pc.draw()
        user = self.user.draw()
        indent = " "*2  # indent at the left side
        space = " "*8   # space between pc and user Grid
        out = indent+"Computer"+" "*24+space+"User\n"
        out += indent+" "*4+"  ".join(pc.columns)+space+" "*4+"  ".join(user.columns)
        for row in range(len(pc)):
            out += "\n"+indent+"{:2d}  ".format(row+1)+"  ".join(pc.iloc[row,:])
            out += space+"{:2d}  ".format(row+1)+"  ".join(user.iloc[row,:])
        return out

    def set_ship_nmbrs(self, ship_nmbrs):
        '''Set custom ship numbers'''
        self.ship_nmbrs = ship_nmbrs
        self.pc.ship_nmbrs = ship_nmbrs
        self.user.ship_nmbrs = ship_nmbrs

    def distribute_ships(self):
        '''Distribute ships on both player and pc grid'''
        self.user.distribute_ships()
        self.pc.distribute_ships()

    def instructions(self):
        '''Print instructions of the battleship game'''
        # TODO
        # Basic introduction to game
        # Printed Grids: what character means what?
        # Possible user inputs
        # How does the computer move?
        return "To be added."

    def create_computer_move(self):
        # TODO: let pc shoot randomly, except a ship is hit
        # TODO: Complete ship destruction in case of hit
        # TODO: Add more sophisticated guesses
        # return field string
        return "dummy field"

    def restart(self):
        '''Restart game. Only saved param is ship_nmbrs'''
        # do not update self.ship_nmbrs as it could be customized
        self.pc = _Grid('computer', self.ship_nmbrs)
        self.user = _Grid('user', self.ship_nmbrs)
        # new ship positions
        self.distribute_ships()

    def remaining_ships(self):
        '''Create a string with information about non-destroyed ships'''
        indent = " "*2
        maxnum = self.ship_nmbrs.max()  # maximum number of ships
        out = indent+"Not destroyed ships (hit ships are included)\n"
        out += indent+"Computer"+' '*4+' '*6    # 6 spaces between pc and user
        if maxnum > 2:
            out += ' '*int((maxnum-2)*6)
        out += "User"
        for i in range(5):
            if self.pc.ship_nmbrs[i] == 0:  # no line needed for not existing ships
                continue
            # save 5 spaces for every ship {:5s} and write 0's for every ship length
            out += '\n'+indent+('{:5s} '.format('0'*(5-i)))*int(self.pc.ship_nmbrs[i]) # pc
            if self.pc.ship_nmbrs[i] < maxnum: # fill space to user ships
                out += (' '*6)*int(maxnum-self.pc.ship_nmbrs[i])
            out += ' '*6+('{:5s} '.format('0'*(5-i)))*int(self.user.ship_nmbrs[i]) # user
        return out
