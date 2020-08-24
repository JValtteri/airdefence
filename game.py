import pygame
import config as config
from pygame import display, image, transform, mouse
from time import sleep
import random
import math

# INIT

pygame.init()
clock = pygame.time.Clock()
display.set_caption('My 2nd PyGame')


# CONFIG
SCREEN_SIZE = config.SCREEN_SIZE
ASSET_SIZE = config.ASSET_SIZE
screen = display.set_mode(SCREEN_SIZE)
SHIP_LOCALE = config.SHIP_LOCALE


# IMAGES
background_img = image.load(config.BACKGROUND).convert()
background_img = transform.scale(background_img, SCREEN_SIZE)

croshair_img = image.load(config.CROSHAIR).convert()
croshair_img.set_colorkey((63,72,204))

bogey_img = image.load(config.BOGEY).convert()
bogey_img.set_colorkey((63,72,204))

missile_img = image.load(config.MISSILE).convert()
missile_img.set_colorkey((63,72,204))

splash_img = image.load(config.SPLASH).convert()
splash_img.set_colorkey((63,72,204))

ship_img = image.load(config.SHIP).convert()
ship_img = transform.scale2x(ship_img)
ship_img.set_colorkey((63,72,204))


class Object():

    def __init__(self, image,
                 x = 0,
                 y = 0,
                 v = 0,
                 vect = (0,0),
                 expire = True,
                 visible = False):

        self.visible = visible
        self.image = image
        self.rect = image.get_rect(center = (x, y))
        self.v = v
        self.u_vect = 0
        self.time = None
        self.expire = expire

        self.u_vector(v, vect)

    def pos(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def move_x(self, delta = None):
        if delta == None:
            delta = self.v
        self.rect.centerx += delta

    def move_y(self, delta = None):
        if delta == None:
            delta = self.v
        self.rect.centery += delta

    def move_2d(self):
        self.move_x(self.v * self.u_vect[0])
        self.move_y(self.v * self.u_vect[1])

    def speed(self, v = 0):
        self.v = v

    def u_vector(self, v, vect):
        x = vect[0]
        y = vect[1]
        l = math.sqrt( x**2 + y**2 )
        try:
            vx = x / l
        except ZeroDivisionError:
            vx = 0
        try:
            vy = y / l
        except ZeroDivisionError:
            vy = 0
        self.u_vect = (vx, vy)

    def draw(self):
        if self.visible == True and self.time is not 0:
            screen.blit(self.image,(self.rect))
            if self.time > 0:
                self.time -= 1


    def show(self, time=None):
        self.time = time
        self.visible = True

    def hide(self):
        self.visible = False

    def splash(self, splash):
        self.image = splash


# FUNCTIONS

def vector(end, start=(0, 0) ):
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]

    return (delta_x, delta_y)


def splash_it(missile, bogey):
    missile.splash(splash_img)
    missile.speed(0)
    missile.show(20)
    missile.expire = True

    bogey.speed(0)
    bogey.show(5)
    bogey.expire = True


def check_collision(bogeys, missiles):
    for bogey in bogeys:
        for missile in missiles:
            if missile.rect.colliderect(bogey.rect) and missile.image is not splash_img:
                splash_it(missile, bogey)


def is_garbage(item):
    return item.expire == True and item.time == 0


def refill_clip(clip):
    if clip < 4:
        clip += 1
    return clip


# SPAWNERS

def spawn_bogey(x, v=10):
    bogey = Object(bogey_img, x, v=v)
    bogey.show(375)
    return bogey


def spawn_missile(vect, v=20):
    missile = Object(
                     image = missile_img,
                     x = SHIP_LOCALE[0],
                     y = SHIP_LOCALE[1],
                     v = v,
                     vect = vect)
    missile.show(300)
    return missile


# OBJECTS
croshair = Object(croshair_img)
bogeys = []
missiles = []
clip = 4
ship = Object(
             image=ship_img,
             x = SHIP_LOCALE[0],
             y = SHIP_LOCALE[1],
             expire = False
             )

ship_rect = ship_img.get_rect(center = (SHIP_LOCALE))
ship.show(-1)


# EVENTS
SPAWNBOGEY = pygame.USEREVENT
pygame.time.set_timer(SPAWNBOGEY,1500)

REFILL = pygame.USEREVENT
pygame.time.set_timer(REFILL,900)


running = True


# GAME LOOP

while running == True:


    # GARBAGE COLLECTION

    missiles = [missile for missile in missiles if not is_garbage(missile)]
    bogeys = [bogey for bogey in bogeys if not is_garbage(bogey)]


    # DRAWING

    screen.blit( background_img, (0,0) )
    ship.draw()
    croshair.draw()

    for bogey in bogeys:
        bogey.move_y()
        bogey.draw()

    for missile in missiles:
        missile.move_2d()
        missile.draw()


    # EVENTS

    current_events = pygame.event.get()
    check_collision(bogeys, missiles)

    for event in current_events:

        # KEYBOARD
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE,
                             pygame.K_ESCAPE,
                             pygame.K_RETURN,
                             pygame.K_KP_ENTER
                             ):
                running = False

        # APP CLOSE
        if event.type == pygame.QUIT:
            running = False

        # MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clip > 0:
                clip -= 1

                mouse_x, mouse_y = mouse.get_pos()
                vect = vector( (mouse_x,mouse_y), SHIP_LOCALE )
                missiles.append( spawn_missile(vect) )

                croshair.pos(mouse_x, mouse_y)
                croshair.show(25)

        # TIMED EVENTS

        if event.type == SPAWNBOGEY:
            bogeys.append( spawn_bogey(
                                       random.randrange(SCREEN_SIZE[0]-64),
                                       random.randrange(5, 15)
                                       ))

        if event.type == REFILL:
            clip = refill_clip(clip)

    display.update()
    clock.tick(25)

print('Goodbye!')
