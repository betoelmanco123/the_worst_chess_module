from useful_trash import *
from board import *


def main():
    positions = initial_postions()

    tablero = board(positions)
    tablero.show_board()


if __name__ == "__main__":
    main()
