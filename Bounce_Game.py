import pygame
from tkinter import *
from tkinter import messagebox
from time import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

width = 850
height = 460
run = 1
right = 1
score = 0

ball = pygame.image.load("img3.png")
balle = pygame.image.load("img4.png")
bg = pygame.image.load("bg.jpg")
pygame.mixer.init()
pygame.mixer.music.load("spring.mp3")
pygame.mixer.music.play(loops = -1)

b_sound = pygame.mixer.Sound("bounce.wav")
h_sound = pygame.mixer.Sound("hit.wav")

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BOUNCE")
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, l, b):
        self.x = x
        self.y = y
        self.l = l
        self.b = b
        self.vel = 7
        self.isJump = 0
        self.jumpC = 10
        self.hitbox = (self.x+6, self.y+5, 50, 50)

    def draws(self, s):
        s.blit(ball, (self.x, self.y))
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        pygame.draw.rect(screen, green, self.hitbox, 1)


class Enemy(object):
    def __init__(self, x, y, l, b):
        self.x = x
        self.y = y
        self.l = l
        self.b = b
        self.vel = 10
        self.hitbox = (self.x+6, self.y+5, 50, 50)

    def draws(self, s):
        s.blit(balle, (self.x, self.y))
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        pygame.draw.rect(screen, green, self.hitbox, 1)


def draw_bounce():
    screen.blit(bg, (0, 0))
    bounce.draws(screen)
    pygame.display.update()


def draw_enemy():
    enemy.draws(screen)
    pygame.display.update()


def redraw():
    screen.blit(bg, (0, 0))
    text = font.render("SCORE : " + str(score), 1, black)
    screen.blit(text, (360, 10))
    bounce.draws(screen)
    enemy.draws(screen)

    pygame.display.update()


bounce = player(50, 400, 64, 64)
enemy = Enemy(700, 400, 64, 64)
fps = 60
font = pygame.font.SysFont('comicsans', 30, 1)

while run:

    pygame.time.delay(100)
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and bounce.x > bounce.vel:
        bounce.x -= bounce.vel
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and bounce.x < width - bounce.b - bounce.vel:
        bounce.x += bounce.vel

    if not (bounce.isJump):
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and bounce.y > bounce.vel:
            bounce.isJump = 1
            b_sound.play()
    else:
        if bounce.jumpC >= -10:
            neg = 1
            if bounce.jumpC < 0:
                neg = -1
            bounce.y -= int((bounce.jumpC ** 2) * 0.7 * neg)
            bounce.jumpC -= 1
        else:
            bounce.isJump = 0
            bounce.jumpC = 10

    if right == 1:
        if enemy.x > enemy.vel:
            enemy.x -= enemy.vel
        else:
            enemy.x += enemy.vel
            score += 10
            right = 0
    else:
        if enemy.x < width - enemy.b - enemy.vel:
            enemy.x += enemy.vel
        else:
            enemy.x -= enemy.vel
            score += 10
            enemy.vel +=5
            right = 1

    if bounce.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and bounce.hitbox[1] + bounce.hitbox[3] > enemy.hitbox[1]:
        if bounce.hitbox[0] + bounce.hitbox[2] > enemy.hitbox[0] and bounce.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
            h_sound.play()
            sleep(1)
            run = 0

    draw_bounce()
    draw_enemy()
    redraw()

    text = font.render("SCORE : " + str(score), 1, black)
    screen.blit(text, (360, 10))

    pygame.display.update()

pygame.quit()

Tk().wm_withdraw()
messagebox.showinfo("GAME RESULT", "Your Score is " + str(score))
