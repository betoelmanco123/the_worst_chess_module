from useful_trash import *
from board import *


def main():
    positions = initial_postions()

    tablero = board(positions)
    tablero.show_board()
    place = tablero.pieces
    for i in place.values():
        if i and i.id == ("pawn", 4, 2):
            print(i.relative_moves(tablero))
            for k in i.relative_moves(tablero):
                test = empty("test")
                if test.color == "black":
                    test.name = "\033[31mT\033[0m"
                else:
                    test.name = "\033[34mT\033[0m"

                tablero.positions[k] = test
    tablero.show_board()
    print("pawn", tablero.pieces[4,2].id)
    print(tablero.move_piece(tablero.pieces[4,2], (4,3), tablero))


if __name__ == "__main__":
    main()
