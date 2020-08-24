import pygame
import config as config
from pygame import display, event, image, transform, mouse
#from config import config
from time import sleep

clock = pygame.time.Clock()

pygame.init()
display.set_caption('My 2nd PyGame')

class Object():

    def __init__(self, asset, x = 0, y = 0, visible = False):
        self.visible = visible
        self.asset = asset
        self.x = x
        self.y = y
        self.time = None

    def pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self, ):
        if self.visible == True and self.time is not 0:
            screen.blit(self.asset,(self.x, self.y))
            self.time -= 1

    def show(self, time=None):
        self.time = time
        self.visible = True

    def hide(self):
        self.visible = False

# CONFIG
SCREEN_SIZE = config.SCREEN_SIZE
screen = display.set_mode(SCREEN_SIZE)

# IMAGES
background = image.load(config.BACKGROUND)
background = transform.scale(background, SCREEN_SIZE)
croshair_img = image.load(config.CROSHAIR)

# OBJECTS
croshair = Object(croshair_img)

running = True

while running == True:
    current_events = event.get()

    screen.blit(background,(0,0))
    croshair.draw()

    for e in current_events:
        if e.type == pygame.KEYDOWN:
            running = False

        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = mouse.get_pos()

            croshair.pos(mouse_x - 32, mouse_y - 32)
            croshair.show(25)

    display.update()
    clock.tick(25)

print('Goodbye!')
