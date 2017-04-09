import pygame, sys
from pygame.locals import *

FPS = 30
fpsClock = pygame.time.Clock()
MOVERATE = 5
S_WIDTH = 300
S_HEIGHT = 400

def createCenteredText(msg):
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurf = fontObj.render(msg, True, GREEN, BLUE)
    textRect = textSurf.get_rect()
    textRect.center = (200, 150)
    return (textSurf, textRect)

def animateCat():
    DISPLAYSURF = pygame.display.set_mode((S_HEIGHT, S_WIDTH), 0, 32)
    pygame.display.set_caption("Animation")
    catImg = pygame.image.load("cat.png")
    catx = 10
    caty = 10
    laserImg = pygame.image.load("laser.png")
    WHITE = (255,255,255)
    text_tuple = createCenteredText("Hello Mofo")
    textSurf = text_tuple[0]
    textRect = text_tuple[1]
    direction = "right"
    cat = {"img": catImg, "x": catx, "y": caty, "direction": ""}
    laser = {"img": laserImg, "x": catx, "y": caty, "direction": ""}
    elems = (cat,)
    while True:
        DISPLAYSURF.fill(WHITE)
        for elem in elems:
            #print "TT: " + str(elems)
        #DISPLAYSURF.blit(textSurf, textRect)
            if elem["direction"] == "right":
                if elem["x"] != 280:
                    elem["x"] += MOVERATE
            elif elem["direction"] == "down":
                if elem["y"] != 220:
                    elem["y"] += MOVERATE
            elif elem["direction"] == "up":
                if elem["y"] != 10:
                    elem["y"] -= MOVERATE
            elif elem["direction"] == "left":
                if elem["x"] != 10:
                    elem["x"] -= MOVERATE
            if (elem["img"]):
                DISPLAYSURF.blit(elem["img"], (elem["x"],elem["y"]))

        for event in pygame.event.get():
            if event.type == QUIT: #QUIT comes from pygame.locals
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key in (K_UP, K_w)):
                    elems[0]["direction"] = "up"
                elif (event.key in (K_DOWN, K_s)):
                    elems[0]["direction"] = "down"
                elif (event.key in (K_LEFT, K_a)):
                    elems[0]["direction"] = "left"
                elif (event.key in (K_RIGHT, K_d)):
                    elems[0]["direction"] = "right"
                elif (event.key == K_c):
                    elems[0]["direction"] = ""
                elif (event.key == K_SPACE):
                    laser = {"img": laserImg, "x": elems[0]["x"], "y": elems[0]["y"], "direction": elems[0]["direction"]}
                    elems = elems + (laser,)
        pygame.display.update()
        fpsClock.tick(FPS)

def main():
    pygame.init()

    animateCat()


if __name__ == "__main__":
    main()