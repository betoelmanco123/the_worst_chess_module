class board:
    def __init__(self, positions: dict):
        self.squares = 64
        self.rows = 8
        self.columns = 8
        self.positions = positions
        self.pieces = positions

    def show_board(self):
        counter = 0
        for key, value in self.positions.items():
            _, y = key
            if counter < y:
                print("\n", end="")
                counter = y
            print(f"{value.name} ", end="")
        print()

    def move_piece(self, piece, position):
        if position in piece.relative_moves:
            self.positions[position] = piece
            self.positions[piece.position] = empty()
        else:
            raise ValueError

    def update_position(self):
        for i in self.positions.values():
            ...


# father class
class piece:
    def __init__(self, color, id):
        self.color = color
        self.id = id
        _, x, y = id
        self.position = (x, y)


# ----
class pawn(piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "P"
        elif color == "black":
            self.name = "p"

    def relative_moves(self, tablero: board):
        _, x, y = self.id
        pieces = tablero.positions.values()
        moves = []
        correct = moves[::]
        # avanzar
        if tablero.positions[(x, y + 1)].color == any:
            correct.append(tablero.positions[x, y + 1].position)
        # capturar
        if (
            tablero.positions[(x + 1, y + 1)].color != "any"
            and tablero.positions[(x + 1, y + 1)].color != self.color
        ):
            correct.append(tablero.positions[(x + 1, y + 1)].position)
        if (
            tablero.positions[(x - 1, y + 1)].color != "any"
            and tablero.positions[(x + 1, y + 1)].color != self.color
        ):
            correct.append(tablero.positions[(x - 1, y + 1)].position)

        return correct


class knigth(piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "N"
        elif color == "black":
            self.name = "n"

    def relative_moves(self, board):
        _, x, y = self.id
        valid_moves = []
        moves = [
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1),
            # -----
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x + 1, y + 2),
            (x - 1, y - 2),
        ]
        for move_x, move_y in moves:
            if 1 <= move_x <= 8 and 1 <= move_y <= 8:
                if board.positions[(move_x, move_y)].color != self.color:
                    valid_moves.append((move_x, move_y))
        print(valid_moves)
        return valid_moves
        # (x +- 3, y +- 1), (x +- 1, y +- 3)


class bishop(piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "B"
        elif color == "black":
            self.name = "b"

    def relative_moves(self, board): 
        _, x, y = self.id
        valid_moves = []

        while x > 0 and y > 0:
            x, y = x -1, y -1
            if board.positions[(x,y)].color == self.color:
                break
            elif board.positions[(x,y)].color == "any":
                valid_moves.append((x,y))
            else :
                valid_moves.append((x,y))
                break
        _, x, y = self.id
        
        while x < 9 and y > 0:
            x, y = x +1, y -1
            if board.positions[(x,y)].color == self.color:
                break
            elif board.positions[(x,y)].color == "any":
                valid_moves.append((x,y))
            else :
                valid_moves.append((x,y))
                break
        _, x, y = self.id
        while x < 9 and y < 9:
            x, y = x +1, y +1
            if board.positions[(x,y)].color == self.color:
                break
            elif board.positions[(x,y)].color == "any":
                valid_moves.append((x,y))
            else :
                valid_moves.append((x,y))
                break
        _, x, y = self.id
        while x > 0 and y < 9:
            x, y = x -1, y +1
            if board.positions[(x,y)].color == self.color:
                break
            elif board.positions[(x,y)].color == "any":
                valid_moves.append((x,y))
            else :
                valid_moves.append((x,y))
                break
        return valid_moves
                
        


class rook(piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "R"
        elif color == "black":
            self.name = "r"


class queen(piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "Q"
        elif color == "black":
            self.name = "q"


class king(piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "K"
        elif color == "black":
            self.name = "k"


class empty(piece):
    def __init__(self, color="any", id=("empty", 1, 2)):
        super().__init__(color, id)
        self.name = "."


def main(): ...


if __name__ == "__main__":
    main()
