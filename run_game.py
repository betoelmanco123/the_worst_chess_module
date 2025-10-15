from board import *
from pathlib import Path
from useful_trash import *
import pygame

pygame.init()
# pygame stuff----
WIDTH = 720
HEIGHT = 720
BOX_SIZE = 90
positions = initial_postions()
pantalla = pygame.display.set_mode((HEIGHT, WIDTH))
running = True
pygame.display.set_caption("Chess")
ASSETS = Path(
    "/Users/robertoromero/Desktop/chess/chess_pieces/"
)  # carpeta donde guardaste los PNG

# Mapea (color, pieza) -> archivo
SPRITES = {
    ("white", "king"): ASSETS / "chess-king-white-256.png",
    ("white", "queen"): ASSETS / "chess-queen-white-256.png",
    ("white", "rook"): ASSETS / "chess-rook-white-256.png",
    ("white", "bishop"): ASSETS / "chess-bishop-white-256.png",
    ("white", "knight"): ASSETS / "chess-knight-white-256.png",
    ("white", "pawn"): ASSETS / "chess-pawn-white-256.png",
    ("black", "king"): ASSETS / "chess-king-black-256.png",
    ("black", "queen"): ASSETS / "chess-queen-black-256.png",
    ("black", "rook"): ASSETS / "chess-rook-black-256.png",
    ("black", "bishop"): ASSETS / "chess-bishop-black-256.png",
    ("black", "knight"): ASSETS / "chess-knight-black-256.png",
    ("black", "pawn"): ASSETS / "chess-pawn-black-256.png",
}
for i in SPRITES:
    image = pygame.image.load(SPRITES[i]).convert_alpha()
    SPRITES[i] = pygame.transform.smoothscale(image, (BOX_SIZE, BOX_SIZE))
image_pawn_white = pygame.image.load(
    "/Users/robertoromero/Desktop/chess/chess_pieces/chess-pawn-white-256.png"
).convert_alpha()
image_pawn_white = pygame.transform.smoothscale(image_pawn_white, (BOX_SIZE, BOX_SIZE))
image_rook_white = pygame.image.load(
    "/Users/robertoromero/Desktop/chess/chess_pieces/chess-rook-white-256.png"
).convert_alpha()
image_rook_white = pygame.transform.smoothscale(image_rook_white, (BOX_SIZE, BOX_SIZE))
# chess stuff-----

tablero = Board(positions)

test = pygame.Rect(20, 20, 20, 20)
turn = 0
rows, columns = 0, 0
squares = []
while rows < 720:
    columns = 0
    while columns < 720:
        value_square = pygame.Rect(rows, columns, BOX_SIZE, BOX_SIZE)
        squares.append(value_square)
        columns += 90
    rows += 90


# Crear un diccionario para almacenar las hitboxes
piece_hitboxes = {}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            # Comprobar todas las hitboxes guardadas
            for piece_pos, rect in piece_hitboxes.items():
                if rect.collidepoint(mouse_pos):
                    piece = tablero.positions[piece_pos]
                    print(f"¡Click en {piece.__class__.__name__} en {piece_pos}!")
                    # Aquí puedes agregar la lógica de selección de pieza
    
    pantalla.fill((0, 0, 0))
    piece_hitboxes.clear()  # Limpiar hitboxes anteriores
    
    for column in range(8):
        for row in range(8):
            square_index = column * 8 + row
            value = column + row
            if value & 1 == 0:
                color = (100, 100, 200)
            else:
                color = (100, 100, 100)
            # draw the pieces
            pygame.draw.rect(pantalla, color, squares[square_index])
            current_piece = tablero.positions[(column, row)]
            if current_piece:
                # Calcular posición para cada tipo de pieza
                if isinstance(current_piece, Pawn):
                    cx = column * BOX_SIZE + BOX_SIZE // 2
                    cy = row * BOX_SIZE + BOX_SIZE // 2 + 5
                    rect = image_pawn_white.get_rect(center=(cx, cy))
                    # Guardar la hitbox
                    piece_hitboxes[(column, row)] = rect
                    # ...resto del código de dibujo...
                    if current_piece.color == "white":
                        pantalla.blit(SPRITES[(("white", "pawn"))], rect)
                    else:
                        pantalla.blit(SPRITES[(("black", "pawn"))], rect)

                # Rook---
                elif isinstance(current_piece, Rook):
                    cx = column * BOX_SIZE + BOX_SIZE // 2
                    cy = row * BOX_SIZE + BOX_SIZE // 2 + 5
                    rect = image_rook_white.get_rect(center=(cx, cy))
                    piece_hitboxes[(column, row)] = rect
                    if current_piece.color == "white":
                        pantalla.blit(SPRITES[("white", "rook")], rect)
                    else:
                        pantalla.blit(SPRITES[("black", "rook")], rect)
                # Knight---
                elif isinstance(current_piece, Knigth):
                    cx = column * BOX_SIZE + BOX_SIZE // 2 + 7
                    cy = row * BOX_SIZE + BOX_SIZE // 2 + 6
                    rect = image_rook_white.get_rect(center=(cx, cy))
                    piece_hitboxes[(column, row)] = rect
                     # Guardar la hitbox
                    if current_piece.color == "white":
                        pantalla.blit(SPRITES[("white", "knight")], rect)
                    else:
                        pantalla.blit(SPRITES[("black", "knight")], rect)
                # Bishop---
                elif isinstance(current_piece, Bishop):
                    cx = column * BOX_SIZE + BOX_SIZE // 2 
                    cy = row * BOX_SIZE + BOX_SIZE // 2 + 6
                    rect = image_rook_white.get_rect(center=(cx, cy))
                    piece_hitboxes[(column, row)] = rect    
                    if current_piece.color == "white":
                        pantalla.blit(SPRITES[("white", "bishop")], rect)
                    else:
                        pantalla.blit(SPRITES[("black", "bishop")], rect)
                # queen---
                elif isinstance(current_piece, Queen):
                    cx = column * BOX_SIZE + BOX_SIZE // 2
                    cy = row * BOX_SIZE + BOX_SIZE // 2 - 5
                    rect = image_rook_white.get_rect(center=(cx, cy))
                    piece_hitboxes[(column, row)] = rect
                    if current_piece.color == "white":
                        pantalla.blit(SPRITES[("white", "queen")], rect)
                    else:
                        pantalla.blit(SPRITES[("black", "queen")], rect)
                # King
                elif isinstance(current_piece, King):
                    cx = column * BOX_SIZE + BOX_SIZE // 2
                    cy = row * BOX_SIZE + BOX_SIZE // 2 + 6
                    rect = image_rook_white.get_rect(center=(cx, cy))
                    piece_hitboxes[(column, row)] = rect
                     # Guardar la hitbox
                    if current_piece.color == "white":
                        pantalla.blit(SPRITES[("white", "king")], rect)
                    else:
                        pantalla.blit(SPRITES[("black", "king")], rect)
                else:
                    print("pieza no reconocida")
                    cx = column * BOX_SIZE
                    cy = row * BOX_SIZE + BOX_SIZE // 2
                    rect = pygame.Rect(cx, cy, BOX_SIZE, BOX_SIZE)
                    piece_hitboxes[(column, row)] = rect
                    pygame.draw.rect(pantalla, (255, 0, 255), rect, 2)  # 2 = grosor
            # Opcional: Dibujar hitboxes para debug
            for rect in piece_hitboxes.values():
                pygame.draw.rect(pantalla, (255, 0, 0), rect, 2)
    
    pygame.display.update()

pygame.quit()
