# install pygame library by using the pip command(pip on win or pip3 on mac)

# import pygame(check if it s works you should after run the file "Hello from pygame community" if you got this all good)
import pygame

FPS = 60

# import the checkers file in the main file
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board
from checkers.game import Game

# Window and caption(name of the app)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_row_cel_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)



    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_cel_from_mouse(pos)

            
        game.update()

    pygame.quit()



main()