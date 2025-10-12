from board import *


def initial_postions():
    positions = {}
    for y in range(8):
        for x in range(8):
            if y == 1:
                positions[(x, y)] = Pawn(color="white", id=("pawn", x, y))
            elif y == 6:
                positions[(x, y)] = Pawn(color="black", id=("pawn", x, y))
            # Pawns
            elif y == 7:
                if x == 0 or x == 7:
                    positions[(x, y)] = Rook(color="black", id=("rook", x, y))
                elif x == 1 or x == 6:
                    positions[(x, y)] = Knigth(color="black", id=("knigth", x, y))
                elif x == 2 or x == 5:
                    positions[(x, y)] = Bishop(color="black", id=("bishop", x, y))
                elif x == 3:
                    positions[(x, y)] = Queen(color="black", id=("queen", x, y))
                else:
                    positions[(x, y)] = King(color="black", id=("king", x, y))
            # ---------------------
            elif y == 0:
                if x == 0 or x == 7:
                    positions[(x, y)] = Rook(color="white", id=("rook", x, y))
                # Knigths

                elif x == 1 or x == 6:
                    positions[(x, y)] = Knigth(color="white", id=("knigth", x, y))
                # bishops

                elif x == 2 or x == 5:
                    positions[(x, y)] = Bishop(color="white", id=("bishop", x, y))
                elif x == 3:
                    positions[(x, y)] = Queen(color="white", id=("queen", x, y))
                else:
                    positions[(x, y)] = King(color="white", id=("king", x, y))
            # empty
            else:
                positions[(x, y)] = None

    return positions


if __name__ == "__main__":
    ...
