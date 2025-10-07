from useful_trash import *
from board import *


def main():
    positions = initial_postions()

    tablero = board(positions)
    tablero.show_board()
    place = tablero.pieces
    for i in place.values():
        if i.id == ("pawn", 4, 6):
            print(i.relative_moves(tablero))
            for k in i.relative_moves(tablero):
                test = empty("test")
                test.name = "\033[31mT\033[0m"
                tablero.positions[k] = test
    tablero.show_board()


if __name__ == "__main__":
    main()
