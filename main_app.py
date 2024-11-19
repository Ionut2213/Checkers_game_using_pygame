# install pygame library by using the pip command(pip on win or pip3 on mac)

# import pygame(check if it s works you should after run the file "Hello from pygame community" if you got this all good)
import pygame

FPS = 60

# import the checkers file in the main file
from checkers.constants import WIDTH, HEIGHT

# Window and caption(name of the app)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")





def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()



main()