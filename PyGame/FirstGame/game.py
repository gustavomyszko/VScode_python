import pygame as pg 

pg.init()
print("----------------------------")
print("action: start!")

#Window Size
WIN_HEIGHT = 800
WIN_WIDTH = 1000
#Window Display
win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("HelloWorld!")

#Rectangle Size
rec_width = 20
rec_height = 20
#Rectangle Attributes
speed = 10
#Rectangle Position
x = int(WIN_WIDTH / 2 - rec_width / 2)
y = int(WIN_HEIGHT / 2 - rec_height / 2)

#When the game is runing -> isPlaying = TRUE
isPlaying = True
while isPlaying:
    #50ms Delay to start
    pg.time.delay(50)

    #Events
    for event in pg.event.get():
        #When the game stops -> isPlaying = FALSE
        if event.type == pg.QUIT:
            isPlaying = False
            print("action: quit")

    #Key Configuration
    keys = pg.key.get_pressed()

    #Keys
    #When the keyboard Key are pressed
    if keys[pg.K_LEFT]:
        x -= speed

    if keys[pg.K_RIGHT]:
        x += speed

    if keys[pg.K_UP]:
        y -= speed

    if keys[pg.K_DOWN]:
        y += speed

    # if keys[pg.K_SPACE]:

    #window fill background   
    win.fill((100,146,40))
    #DRAW window
    #ball
    pg.draw.rect(win, ('blue'), (x, y, rec_width, rec_height))

    #UPDATE display
    pg.display.update()

#Quit WHILE loop
pg.quit()