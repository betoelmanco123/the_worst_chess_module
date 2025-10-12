from board import *
from useful_trash import *
import pygame
pygame.init()
#pygame stuff----
WIDTH = 720
HEIGHT = 720
positions = initial_postions()
pantalla = pygame.display.set_mode((HEIGHT, WIDTH))
running = True
#chess stuff-----

tablero = board(positions)

turn = 0
value_square = pygame.Rect(100, 100, 90, 90)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pantalla.fill((0, 0, 0))  
    # dibujar cosas aquí...
    pygame.draw.rect(pantalla, (100,100,200), value_square )
    pygame.display.update()   

pygame.quit()

