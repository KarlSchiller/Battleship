import argparse
import pandas as pd
import numpy as np
from pprint import pprint


class grid():
    '''Holds one battleship grid'''
    def __init__(self):
        self.board = pd.DataFrame(False,
                index=np.arange(start=1, stop=11),
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.shot = [[False]*10]*10


    def __str__(self):
        '''Print grid to console'''
        pretty = self.board.replace(to_replace=False, value='~')
        pretty.replace(to_replace=True, value='x', inplace=True)
        return pretty.to_string()


def print_instructions():
    '''Print instructions of the battleship game'''
    print("To be added.")


def print_welcome():
    '''Print welcome message to the battleship game'''
    print("To be added.\n")


def main(args):

    if args.instructions:
        print_instructions()

    print_welcome()
    user = grid()
    print(user)
    pprint(user.shot)


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
