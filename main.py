from pygame import *
from random import *
from os import *

point = 0
background = image.load(path.join("images", "background.png"))
background_X = 0
background_X2 = background.get_width()
a_bird_up = image.load(path.join("images", "bird_wing_up.png"))
a_bird_down = image.load(path.join("images", "bird_wing_down.png"))
birdY = 256
birdX = 40
pipe_top = image.load(path.join("images", "pipe_end.png"))
pipe_body = image.load(path.join("images", "pipe_body.png"))
red = (255, 0, 0)
blue = (0, 0, 255)

wallX = 280

#need for speed
FPS= 60
init()
main = display.set_mode((280, 512))
display.set_caption("Flappy Bird")
#clock
clock = time.Clock()
speedPipe = 1


class bird():
    UpDown = [a_bird_up, a_bird_down]

    def __init__(self):
        self.x = birdX
        self.y = birdY
        self.jump = False
        self.imageCount = 0
        self.jumpCount = 0

    def draw(self):
        if self.jump:
            self.y -= 2
            self.jumpCount += 1
        else:
            self.y += 1
        if self.jumpCount >= 20:
            self.jump = False
            self.jumpCount = 0
        main.blit(self.UpDown[self.imageCount], (self.x, self.y))
        self.imageCount += 1
        if self.imageCount > 1:
            self.imageCount = 0


class pipe():
    def __init__(self):
        self.x = wallX
        self.piece_top = randint(3, 8)
        self.piece_bot = 16 - 6 - self.piece_top
        self.point = point
        self.speed = speedPipe

    def draw(self):
        global fin
        for i in range(0, self.piece_bot):  #cột trên
            pos = (self.x, i * 32)
            main.blit(pipe_body, pos)
        pos_top = (self.x, (i + 1) * 32)
        main.blit(pipe_top, pos_top)

        for i in range(0, self.piece_top):  #cột dưới
            pos = (self.x, 512 - i * 32)
            main.blit(pipe_body, pos)
        pos_bot = (self.x, 512 - (i + 1) * 32)
        main.blit(pipe_top, pos_bot)
        #look at this

        if self.x <= the_bird.x and the_bird.x >= self.x:  #kiểm tra va chạm
            if pos_top[1] >= the_bird.y or pos_bot[1] <= the_bird.y:
                print("\033[1;31;45m Game over  \n\n")
                fin = True
        if self.x <= -80:
            self.x = 280
            self.piece_top = randint(3, 8)
            self.piece_bot = 16 - 6 - self.piece_top
            self.speed += 0.2
            self.point += 1
            print("\n\n\033[1;32;45m Speed of pipe:", self.speed, "\n\n")
            print("\n\n\033[1;33;45m Point:", self.point, "\n")
            '''print("\033[1;32;45m Bright Green  \n\n")'''
            main.blit(text, (0, 0))


the_bird = bird()
fin = False
up_pipe = pipe()
while not fin:
    for e in event.get():
        if e.type == QUIT:
            fin = True
        if e.type == KEYDOWN:
            if e.key == K_SPACE or e.key == K_UP or e.key == K_w:
                if the_bird.jump == False:
                    the_bird.jump = True
    if the_bird.y >= 512:
        print("\n\033[1;31;45mYou have gone to the bottom\n => Game over\n")
        fin = True
    if the_bird.y <= 0:
        print("\n\033[1;31;45mYou have gone to the top\n => Game over\n")
        fin = True

    background_X -= 1
    background_X2 -= 1
    if background_X <= -280:
        background_X = 280
    if background_X2 <= -280:
        background_X2 = 280

    main.blit(background, (background_X, 0))
    main.blit(background, (background_X2, 0))
    the_bird.draw()
    up_pipe.draw()
    fo = font.Font("freesansbold.ttf", 20)  #point label
    text = fo.render("Points: " + str(up_pipe.point), True, red)
    main.blit(text, (0, 0))
    up_pipe.x -= up_pipe.speed

    clock.tick(FPS)
    display.update()
