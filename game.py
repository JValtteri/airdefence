import pygame
import config as config
from pygame import display, image, transform, mouse
from time import sleep
import random

clock = pygame.time.Clock()

pygame.init()
display.set_caption('My 2nd PyGame')

class Object():

    def __init__(self, asset, x = 0, y = 0, v = 0, visible = False):
        self.visible = visible
        self.asset = asset
        self.x = x
        self.y = y
        self.v = v
        self.time = None

    def pos(self, x, y):
        self.x = x
        self.y = y

    def move_x(self, delta = None):
        if delta == None:
            delta = self.v
        self.x += delta

    def move_y(self, delta = None):
        if delta == None:
            delta = self.v
        self.y += delta

    def speed(self, v):
        self.v == v

    def draw(self):
        if self.visible == True and self.time is not 0:
            screen.blit(self.asset,(self.x, self.y))
            if self.time > 0:
                self.time -= 1

    def show(self, time=None):
        self.time = time
        self.visible = True

    def hide(self):
        self.visible = False

def create_bogey(x, v=10):
    bogey = Object(bogey_img, x, v= v)
    bogey.show(-1)
    #print("bogey", v)
    return bogey


# CONFIG
SCREEN_SIZE = config.SCREEN_SIZE
ASSET_SIZE = config.ASSET_SIZE
screen = display.set_mode(SCREEN_SIZE)

# IMAGES
background_img = image.load(config.BACKGROUND).convert()
background_img = transform.scale(background_img, SCREEN_SIZE)

croshair_img = image.load(config.CROSHAIR).convert()
croshair_img.set_colorkey((63,72,204))

bogey_img = image.load(config.BOGEY).convert()
bogey_img.set_colorkey((63,72,204))

splash_img = image.load(config.SPLASH).convert()
splash_img.set_colorkey((63,72,204))

ship_img = image.load(config.SHIP).convert()
ship_img = transform.scale2x(ship_img)
ship_img.set_colorkey((63,72,204))


#croshair_img.set_colorkey((0,0,0))

# OBJECTS
croshair = Object(croshair_img)
bogeys = []

# EVENTS
SPAWNBOGEY = pygame.USEREVENT
pygame.time.set_timer(SPAWNBOGEY,1500)

running = True

while running == True:
    current_events = pygame.event.get()

    screen.blit( background_img, (0,0) )
    screen.blit( ship_img, ( SCREEN_SIZE[0] / 2 - ASSET_SIZE[0], SCREEN_SIZE[1] - 200 ) )

    croshair.draw()
    for bogey in bogeys:
        bogey.move_y()
        bogey.draw()

    for event in current_events:
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, 
                             pygame.K_ESCAPE,
                             pygame.K_RETURN
                             ):
                running = False

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = mouse.get_pos()

            croshair.pos(mouse_x - 32, mouse_y - 32)
            croshair.show(25)

        if event.type == SPAWNBOGEY:
            bogeys.append( create_bogey( 
                                       random.randrange(SCREEN_SIZE[0]-64),
                                       random.randrange(5, 15) 
                                       ))

    display.update()
    clock.tick(25)

print('Goodbye!')
