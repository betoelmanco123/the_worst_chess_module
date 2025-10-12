class PositionError(Exception):
    def __init__(self, mensaje, codigo):
        super().__init__(mensaje)
        self.codigo = codigo

class Board:
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
            if value:
                print(f"{value.name} ", end="")
            else:
                print(". ", end="")
        print()

    def move_piece(self, piece, position, board):
        print(f"Current position: {piece.position}")
        print(f"Possible moves: {piece.relative_moves(board)}")
        
        if position in piece.relative_moves(board):
            # Actualizar el diccionario de posiciones
            self.positions[position] = piece
            self.positions[piece.position] = None
            
            # Actualizar la posición de la pieza
            _, x, y = piece.id
            piece.position = position
            piece.id = (piece.id[0], position[0], position[1])
        else:
            print(f"Invalid move. Valid moves are: {piece.relative_moves(board)}")
            raise ValueError("Invalid move")

# this class is able to have 2 possible states
# 1. store a object from the class piece
# 2. being empty


class Square:
    def __init__(self, color, coords: tuple, object_piece=None):
        self.color = color
        self.piece = object_piece
        self.position = coords
        if object_piece:
            self.state = True
        else:
            self.state = False


# father class
class Piece:
    def __init__(self, color, id):

        self.color = color

        self.id = id
        _, x, y = id
        self.position = (x, y)
    

        


class empty(Piece):
    def __init__(self, color="any", id=("empty", 1, 2)):
        super().__init__(color, id)

        self.name = "."


# ----
class Pawn(Piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "P"
        elif color == "black":
            self.name = "p"

    # moves that the piece is able to do
    def relative_moves(self, tablero: Board):
        _, x, y = self.id
        moves = []

        if self.color == "white":
            # avanzar
            if 1 <= y + 1 <= 8 and not tablero.positions[(x, y + 1)]:
                moves.append((x, y + 1))
            # capturar
            if 1 <= x + 1 <= 8 and 1 <= y + 1 <= 8:
                if tablero.positions.get((x + 1, y + 1)) and tablero.positions[(x + 1, y + 1)].color != self.color:
                    moves.append((x + 1, y + 1))
            if 1 <= x - 1 <= 8 and 1 <= y + 1 <= 8:
                if tablero.positions.get((x - 1, y + 1)) and tablero.positions[(x - 1, y + 1)].color != self.color:
                    moves.append((x - 1, y + 1))
    
        elif self.color == "black":
            # avanzar
            if 1 <= y - 1 <= 8 and not tablero.positions[(x, y - 1)]:
                moves.append((x, y - 1))
            # capturar
            if 1 <= x + 1 <= 8 and 1 <= y - 1 <= 8:
                if tablero.positions.get((x + 1, y - 1)) and tablero.positions[(x + 1, y - 1)].color != self.color:
                    moves.append((x + 1, y - 1))
            if 1 <= x - 1 <= 8 and 1 <= y - 1 <= 8:
                if tablero.positions.get((x - 1, y - 1)) and tablero.positions[(x - 1, y - 1)].color != self.color:
                    moves.append((x - 1, y - 1))

        return moves


class Knigth(Piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "N"
        elif color == "black":
            self.name = "n"

    def relative_moves(self, board):
        _, x, y = self.id
        valid_moves = []
        # al the posible moves
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
        # cleanning the moves that are not allowed for obstructions
        for move_x, move_y in moves:
            if 1 <= move_x <= 8 and 1 <= move_y <= 8:
                if not board.positions[(move_x, move_y)]:
                    valid_moves.append((move_x, move_y))
                elif board.positions[(move_x, move_y)].color != self.color:
                    valid_moves.append((move_x, move_y))
        return valid_moves


class Bishop(Piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "B"
        elif color == "black":
            self.name = "b"

    # scanning the posible postions that are avaible in the direction
    # defined by delta x and delta y
    def _scan_position(self, board, deltas: tuple):
        dx, dy = deltas
        _, x, y = self.id
        valid_moves = []
        x, y = x + dx, y + dy
        while 0 < x <= 8 and 0 < y <= 8:

            if not board.positions[(x, y)]:
                valid_moves.append((x, y))
            elif board.positions[(x, y)].color == self.color:
                break
            else:
                valid_moves.append((x, y))
                break
            x, y = x + dx, y + dy
        return valid_moves

    def relative_moves(self, board):
        # going trougth all the variations of deltas that are useful for us
        valid_moves = []
        permutations = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        for i in permutations:
            aux = self._scan_position(board, i)
            valid_moves.extend(aux)

        return valid_moves


class Rook(Piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "R"
        elif color == "black":
            self.name = "r"

    def _scan_position(self, board, deltas: tuple):
        dx, dy = deltas
        _, x, y = self.id
        valid_moves = []
        x, y = x + dx, y + dy
        while 1 <= x <= 8 and 1 <= y <= 8:
            if not board.positions[(x, y)]:
                valid_moves.append((x, y))
            elif board.positions[(x, y)].color == self.color:
                break
            else:
                valid_moves.append((x, y))
                break
            x, y = x + dx, y + dy
        return valid_moves

    def relative_moves(self, board):
        valid_moves = []
        permutations = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in permutations:
            aux = self._scan_position(board, i)
            valid_moves.extend(aux)

        return valid_moves


class Queen(Piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "Q"
        elif color == "black":
            self.name = "q"

    def _scan_position(self, board, deltas: tuple):
        dx, dy = deltas
        _, x, y = self.id
        valid_moves = []
        x, y = x + dx, y + dy
        while 1 <= x <= 8 and 1 <= y <= 8:
            if not board.positions[(x, y)]:
                valid_moves.append((x, y))
            elif board.positions[(x, y)].color == self.color:
                break
            else:
                valid_moves.append((x, y))
                break
            x, y = x + dx, y + dy
        return valid_moves

    def relative_moves(self, board):
        valid_moves = []
        permutations = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (-1, -1),
            (1, -1),
            (1, 1),
            (-1, 1),
        ]
        for i in permutations:
            aux = self._scan_position(board, i)
            valid_moves.extend(aux)

        return valid_moves


class King(Piece):
    def __init__(self, color, id):
        super().__init__(color, id)
        if color == "white":
            self.name = "K"
        elif color == "black":
            self.name = "k"

    def relative_moves(self, board):
        _, x, y = self.id
        permutations = [
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y - 1),
            (x + 1, y),
            (x - 1, y),
        ]
        correct = []
        for i in permutations:
            if not board.positions[i]:
                correct.append(i)
            elif board.positions[i].color != self.color:
                correct.append(board.positions[i].position)

        return correct


def main(): ...


if __name__ == "__main__":
    main()
