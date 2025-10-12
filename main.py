from useful_trash import *
from board import *


def main():
    positions = initial_postions()

    tablero = Board(positions)
    tablero.show_board()
    place = tablero.pieces

    tablero.show_board()
    
    print(tablero.move_piece(tablero.pieces[1,0], (2,2), tablero))
    tablero.show_board()

if __name__ == "__main__":
    main()
