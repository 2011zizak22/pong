import pygame
import time

pygame.init()
pygame.win = pygame.display.set_mode((100, 200)) # pygame.display.set_mode((width, height))
r = pygame.Rect(10, 5, 100, 50) # pygame.Rect(left, top, width, height)
pygame.draw.rect(pygame.win, (255, 0, 0), r) # pygame.draw.rect(surface, (R, G, B), Rectangle) 
pygame.display.update()
time.sleep(5)
pygame.draw.circle(pygame.win, (0, 255, 0), (50, 100), 10)
pygame.display.update()
time.sleep(20)