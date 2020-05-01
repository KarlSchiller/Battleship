from pandas import DataFrame


class grid():
    '''Holds one battleship grid'''
    # TODO: explain attributes
    def __init__(self, player):
        self.game_over = False  # set to True if all ships are hit
        self.board = DataFrame(False,
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.shots = [[False]*10]*10    # shots taken
        self.player = player    # pc or user
        # TODO: add attribute that holds remaining ships
        # TODO: distribute ships on self.board

    def draw(self):
        # TODO: pc grid: place '?' for all field that have not been shot yet
        # TODO: user grid: write 0 for all non shot ships and ' '  for all non shot oceans
        matrix = self.board.replace(to_replace=False, value='~')
        matrix.replace(to_replace=True, value='x', inplace=True)
        return matrix

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
        # TODO: print both grid next to each other
        return "Computer\n"+str(self.pc)+"\n\nUser\n"+str(self.user)

    def distribute_ships(self):
        # TODO: Distribute ships
        pass

    def instructions(self):
        '''Print instructions of the battleship game'''
        # TODO
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
