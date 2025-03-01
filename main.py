import pygame as pg
import sys as s



pg.init()
black = (0,0,0)
white = (255,255,255)
width = 1200
height = 600
cost = 0
costs = [10, 50, 100, 500]
click_value = 1
photos = ["shadowsad.png", "shadow.png", "shadow2.png", "shadow5.png"]
photo = 0

screen = pg.display.set_mode((width, height))
Map = pg.transform.scale(pg.image.load(photos[photo]), size=(1200, 600))
pg.display.set_caption("shadowtaptaptap")
plus = pg.transform.scale(pg.image.load("ring2.png"), size=(120,100))

score = 0
power = 1
font = pg.font.Font(None, 36)

while True:
    screen.fill(white)
    screen.blit(Map, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            s.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if score >= costs[cost]:
                click_value += 2
                score -= costs[cost]
                cost +=1
                photo += 1
                Map = pg.transform.scale(pg.image.load(photos[photo]), size=(1200, 600))



        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                screen.blit(plus, (850,250))
                score += click_value
                pg.mixer.music.load("sonicring.mp3")
                pg.mixer.music.play(1)



    text = font.render(f"{score}",  True, "red")
    screen.blit(text, (300, 200))
    apelisin = font.render(("колец"), True, "yellow")
    screen.blit(apelisin, (300, 220))

    pg.display.flip()

    pg.time.Clock().tick(10)