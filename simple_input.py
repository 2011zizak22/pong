import pygame as pg
import sys

def get_input():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type  == pg.KEYDOWN:
           if event.key == pg.K_LEFT:
               print("<-")
           elif event.key == pg.K_RIGHT:
               print("->")


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((512,384))
    try:
        while True:
            get_input()
    except KeyboardInterrupt:
        print("exiting...")
