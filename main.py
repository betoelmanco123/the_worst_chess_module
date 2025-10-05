from useful_trash import *
from board import *


def main():
    positions = initial_postions()

    tablero = board(positions)
    tablero.show_board()
    place = tablero.pieces
    for i in place.values():
        if i.id == ('pawn', 4,2):
            print(i.relative_moves())


if __name__ == "__main__":
    main()
