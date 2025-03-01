import pygame as pg
import sys as s



pg.init()

white = (255, 255, 255)

width = 1200
height = 600
screen = pg.display.set_mode((width, height))

font = pg.font.Font(None, 36)
counter = 1
# то что происходит во время игры
while True:
    screen.fill(white)

    for event in pg.event.get():


        if event.type == pg.QUIT:
            print("вы вышли!")
            pg.quit()
            s.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("вы нажали", counter)
                counter += 1


    text = font.render(f"{counter}", True, "red")
    screen.blit(text, (width//2, height//10))

    pg.display.flip()
    pg.time.Clock().tick(60)
