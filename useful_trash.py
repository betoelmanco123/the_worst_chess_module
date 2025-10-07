from board import *


def initial_postions():
    positions = {}
    for y in range(1, 9):
        for x in range(1, 9):
            if y == 2:
                positions[(x, y)] = pawn(color="white", id=("pawn", x, y))
            elif y == 7:
                positions[(x, y)] = pawn(color="black", id=("pawn", x, y))
            # Pawns
            elif y == 8:
                if x == 1 or x == 8:
                    positions[(x, y)] = rook(color="black", id=("rook", x, y))
                elif x == 2 or x == 7:
                    positions[(x, y)] = knigth(color="black", id=("knigth", x, y))
                elif x == 3 or x == 6:
                    positions[(x, y)] = bishop(color="black", id=("bishop", x, y))
                elif x == 4:
                    positions[(x, y)] = queen(color="black", id=("queen", x, y))
                else:
                    positions[(x, y)] = king(color="black", id=("king", x, y))
            # ---------------------
            elif y == 1:
                if x == 1 or x == 8:
                    positions[(x, y)] = rook(color="white", id=("rook", x, y))
                # Knigths

                elif x == 2 or x == 7:
                    positions[(x, y)] = knigth(color="white", id=("knigth", x, y))
                # bishops

                elif x == 3 or x == 6:
                    positions[(x, y)] = bishop(color="white", id=("bishop", x, y))
                elif x == 4:
                    positions[(x, y)] = queen(color="white", id=("queen", x, y))
                else:
                    positions[(x, y)] = king(color="white", id=("king", x, y))
            # empty
            else:
                positions[(x, y)] = empty(color="any", id=("empty", x, y))
    positions[(4, 6)] = pawn(color="black", id=("pawn", 4, 6))
    return positions


if __name__ == "__main__":
    ...
