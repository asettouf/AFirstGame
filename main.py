import pygame, sys
from pygame.locals import *

def hello():
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Hello World")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #QUIT comes from pygame.locals
                pygame.quit()
                sys.exit()
        pygame.display.update

def main():
    pygame.init()
    hello()


if __name__ == "__main__":
    main()