from useful_trash import *
from board import *


def main():
    positions = initial_postions()

    tablero = board(positions)
    tablero.show_board()
    place = tablero.pieces

    tablero.show_board()
    
    print(tablero.move_piece(tablero.pieces[2,1], (3,3), tablero))
    tablero.show_board()

if __name__ == "__main__":
    main()
