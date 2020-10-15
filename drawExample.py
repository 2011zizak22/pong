import pygame
import time

table = {"height": 400, "width": 600}
ball = {"y": table['height']//2,"x": table['width']//2, "dx":1, "dy":-1, "r":1}
paddleL = {"length": table['height']//10, "width": table['width']//100, "x": 0, "y": 0, "dy": 2}
paddleR = {"length": table['height']//10, "width": table['width']//100, "x": table['width'], "y": 0, "dy": 2}

def main():
    pygame.init()
    pygame.win = pygame.display.set_mode((table["width"], table["height"])) # pygame.display.set_mode((width, height))
    r = pygame.Rect(paddleR["x"] - paddleR["width"], paddleR["y"], paddleR["width"], paddleR["length"]) # pygame.Rect(left, top, width, height)
    l = pygame.Rect(paddleL["x"], paddleL["y"], paddleL["width"], paddleL["length"]) # pygame.Rect(left, top, width, height)
    pygame.draw.rect(pygame.win, (255, 0, 0), r) # pygame.draw.rect(surface, (R, G, B), Rectangle)
    pygame.draw.rect(pygame.win, (255, 0, 0), l) # pygame.draw.rect(surface, (R, G, B), Rectangle) 
    pygame.display.update()
    time.sleep(5)
    pygame.draw.circle(pygame.win, (0, 255, 0), (ball["x"], ball["y"]), ball["r"]) # pygame.draw.circle(surface, (R, G, B), (x, y), radius)
    pygame.display.update()
    time.sleep(5)

if __name__ == "__main__":
    main()