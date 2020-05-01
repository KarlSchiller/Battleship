import argparse
from pandas import DataFrame
from time import sleep
from pprint import pprint


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


def main(args):

    # Initialize game
    bs = Battleship()

    if args.instructions:
        print(bs.instructions())
        return

    # game with custom ship numbers
    if args.custom:
        # TODO: Ask the number of every ship type
        # TODO: Update bs.ships list accordingly
        # TODO: Check, if number does not exceed a certain limit
        bs.ships[3] = 5 # dummy
        print("Custom ship number dummy text")
        print(bs.ships)

    # distribute ships on both pc and user grids
    bs.distribute_ships()

    print("Game started.")

    while(1):   # game routine

        # print game board status
        print(bs)

        # For testing purposes
        #  print(bs.user)
        #  pprint(bs.user.shots)

        # prevent pc from playing after inputs restart/ships/quit->no
        user_turn = True
        while(user_turn):
            shot = input("Please enter field(e.g. E5)/ships/quit/restart: ").lower()
            # lower characters to limit possibilities

            # play game
            if (shot[0] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) and (len(shot)>=2):
                if shot[1:] in ['1','2','3','4','5','6','7','8','9','10']:
                    res = bs.user.shoot(shot[0].upper(), shot[1:])
                    #  print('row {}\ncol {}'.format(shot[0].upper(), shot[1:]))   # dummy
                    sleep(1)
                    print(res)
                    sleep(1)
                    user_turn = False
                else:
                    print("Row number has to be between 1 and 10.")

            # restart game
            elif shot in ["restart", "r"]:
                bs.restart()

            # quit game
            elif shot in ["quit", "q"]:
                while(1):
                    confirmation = input("Do you really want to quit game? (yes/y/Y/no/n/N) ")
                    if confirmation.lower() in ["yes", "y"]:
                        return
                    elif confirmation.lower() in ["no", "n"]:
                        break

            # print remaining ships
            elif shot in ["ships", "s"]: # print remaining ships
                print(bs.remaining_ships())

            # no pattern matched
            else:
                print("No pattern matched. Please try again.")

        # calculate computer move
        pc_move = bs.create_computer_move()
        print("Computer chooses field: "+ pc_move)
        sleep(1)
        # execute computer move
        res = bs.pc.shoot(pc_move[0], pc_move[1:])
        # print shoot result
        print(res)
        sleep(1)

        # TODO: check, if user or pc or both have won
        # TODO: print final board and exit loop


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="The battleship boardgame for the terminal.")
    parser.add_argument("-i", "--instructions", action="store_true",
            help="Display game instructions.")
    #  group = parser.add_mutually_exclusive_group()   # either verbose or quiet
    #  group.add_argument("-v", "--verbose", action="store_true",
            #  help="increase output verbosity")
    #  group.add_argument("-q", "--quiet", action="store_true",
            #  help="decrease output verbosity")
    parser.add_argument("-c", "--custom", action="store_true",
            help="Play with a custom fleet.")

    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: User quit the game. Thanks for playing!")
