import argparse
from time import sleep
from battleship import Battleship


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

    print("Game started.\n")

    while(1):   # game routine

        # print game board status
        print(bs, "\n")

        # prevent pc from playing after inputs restart/ships/quit->no
        user_turn = True
        while(user_turn):
            shot = input("Please enter field(e.g. E5)/ships/quit/restart: ").upper()
            # upper characters to limit possibilities

            # play game
            if (shot[0] in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]) and (len(shot)>=2):
                if shot[1:] in ['1','2','3','4','5','6','7','8','9','10']:
                    res = bs.user.shoot(shot)
                    #  print('row {}\ncol {}'.format(shot[0].upper(), shot[1:]))   # dummy
                    sleep(1)
                    print(res)
                    sleep(1)
                    if not res == 'Field is already shot':
                        user_turn = False
                else:
                    print("Row number has to be between 1 and 10.")

            # restart game
            elif shot in ["RESTART", "R"]:
                bs.restart()

            # quit game
            elif shot in ["QUIT", "Q"]:
                while(1):
                    confirmation = input("Do you really want to quit game? (yes/y/Y/no/n/N) ")
                    if confirmation.lower() in ["yes", "y"]:
                        return
                    elif confirmation.lower() in ["no", "n"]:
                        break

            # print remaining ships
            elif shot in ["SHIPS", "S"]: # print remaining ships
                print(bs.remaining_ships())

            # no pattern matched
            else:
                print("No pattern matched. Please try again.")

        # calculate computer move
        pc_move = bs.create_computer_move()
        print("Computer chooses field: "+ pc_move)
        sleep(1)
        # execute computer move
        #  res = bs.pc.shoot(pc_move)
        # print shoot result
        #  print(res, "\n")
        sleep(1)

        # check if one party has won
        if bs.user.game_over:
            if bs.pc.game_over:
                print("DRAW! All ships are destroyed! What a game...")
            else:
                print("VICTORY! Congratulations, you have destroyed all ships!")
            break
        elif bs.pc.game_over:
            print("DEFEAT! Computer has found all of your ships!")
            break


def test():
    # Initialize game
    bs = Battleship()

    bs.user.board.iloc[5:8, 2] = True
    bs.user.board.iloc[2][5:9] = True
    bs.user.shots[:,7:10] = True

    bs.pc.board.iloc[5:8, 2] = True
    bs.pc.board.iloc[2][5:9] = True
    bs.pc.shots[:,7:10] = True

    print(bs.user.board)
    print(bs.user.shots)
    # print game board status
    print(bs)


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

    #  test()

    try:
        main(args)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: User quit the game. Thanks for playing!")
