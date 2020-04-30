import argparse
import pandas as pd
import numpy as np
from time import sleep
from pprint import pprint


class grid():
    '''Holds one battleship grid'''
    def __init__(self):
        self.game_over = False  # set to True if all ships are hit
        self.board = pd.DataFrame(False,
                index=np.arange(start=1, stop=11),
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.shots = [[False]*10]*10
        # TODO: add attribute that holds remaining ships
        # TODO: distribute ships on self.board
        # TODO: add attribute to check if player is pc or user

    def __str__(self):
        '''Print grid to console'''
        # TODO: place '?' for all field that have not been shot yet if grid is from pc
        # TODO: user grid: write 0 for all non shot ships and ' '  for all non shot oceans
        pretty = self.board.replace(to_replace=False, value='~')
        pretty.replace(to_replace=True, value='x', inplace=True)
        return pretty.to_string(header=True, index=True)

    def shoot(self, row, col):
        '''Shoot at a field (row, col) and return ocean or hit'''
        print('row {}\ncol {}'.format(row,col))
        # TODO: Update shots
        # TODO: check, if a ship is hit
        # TODO: check if ship is destroyed
        # TODO: update ships attribute in case of destruction
        # TODO: check if game is over
        # TODO: return ocean, hit ,destroyal or game_over


def print_instructions():
    '''Print instructions of the battleship game'''
    print("To be added.")
    # TODO


def custom_ships(ships):
    '''Let the user define custom ship numbers'''
    ships[3] = 5 # works!
    # TODO: Ask the number of every ship type
    # TODO: Update ships list accordingly
    # TODO: Check, if number does not exceed a certain limit


def init_game(ships):
    '''Initialise game'''
    # TODO: Initialise ship attribute of user and pc with param ships
    user = grid()
    pc = grid()
    # TODO: Distribute ships
    return (pc, user)


def main(args):

    if args.instructions:
        print_instructions()
        return

    # number of ships. First index are ships of size one, second of size two etc.
    ships = [2,2,1,1,1] # default values

    # game with custom ship numbers
    if args.custom:
        custom_ships(ships)

    # pc holds the grid with ships of the user, hence the grid the pc shoots at
    # user holds the grid with ships of the pc, hence the grid the user shoots at
    pc, user = init_game(ships)
    #  print(user)
    #  pprint(user.shots)

    print("Game started.")

    while(1):

        print("Computer\n", pc)
        print("\nUser\n",user)
        shot = input("Please enter field(e.g. E5)/ships/quit/restart: ")

        if len(shot) < 2:
            print("Invalid input. Please try again.")
            continue

        # play the game. it's fun!
        if shot[1] in ['1','2','3','4','5','6','7','8','9','10']:
            if shot[0] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
                user.shoot(shot[0].upper(), shot[1])
                # TODO: print return of shoot: ocean, hit or destroyal or game_over
                sleep(1)

        # restart game
        if shot == "restart":
            # TODO: let the game restart (with new ship positions ^^)
            continue

        # print remaining ships
        if shot == "ships":
            # TODO: print remaining ships of pc and user
            # TODO: create method in class grid to print remaining ships
            pass

        # end game
        if shot == "quit":
            while(1):
                confirmation = input("Do you really want to quit game? (yes/y/Y/no/n/N) ")
                if confirmation in ["yes", "y", "Y"]:
                    return
                elif confirmation in ["no", "n", "N"]:
                    break

        # TODO: let pc shoot randomly, except a ship is hit
        print("Computer chooses field dummy text")
        sleep(1)
        # TODO: print shoot result
        print("Shoot result dummy text.")
        sleep(1)


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

    main(args)
