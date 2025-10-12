from board import *
from useful_trash import *
import pygame
pygame.init()
#pygame stuff----
WIDTH = 720
HEIGHT = 720
BOX_SIZE = 90
positions = initial_postions()
pantalla = pygame.display.set_mode((HEIGHT, WIDTH))
running = True
pygame.display.set_caption("Chess")
#chess stuff-----

tablero = board(positions)

test = pygame.Rect(20, 20, 20,20)
turn = 0
rows, columns = 0,0 
squares = []
while rows < 720:
    columns = 0
    while columns < 720:
        value_square = pygame.Rect(rows, columns, BOX_SIZE, BOX_SIZE)
        squares.append(value_square)
        columns += 90
    rows += 90
print(len(squares))
        

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pantalla.fill((0, 0, 0))  
    # dibujar cosas aquí...
    number = 0
    # draw the a grid 8X8
    for column in range(8):
        for row in range(8):
            square_index = column * 8 + row
            value = column + row
            if value & 1 == 0:
                color = (100,100,200)
            else:
                color = (100,100,100)
            #draw the pieces
            pygame.draw.rect(pantalla, color, squares[square_index])
            if tablero.positions[(column, row)]:
                left = column * 90 + 20
                top = row  * 90 + 20
                if type(tablero.positions[(column, row)]) == pawn:
                    print("pawn")
                test = pygame.Rect(left, top, 20,20)
                pygame.draw.rect(pantalla, (255,255,255), test)
        

        
    pygame.display.update()   

pygame.quit()

