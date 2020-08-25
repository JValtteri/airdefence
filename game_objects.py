import math
from pygame import image, transform
import config

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

    def draw(self, screen):
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


class Images():

    def __init__(self):

        # IMAGES
        self.background_img = image.load(config.BACKGROUND).convert()
        self.background_img = transform.scale(self.background_img, config.SCREEN_SIZE)

        self.croshair_img = image.load(config.CROSHAIR).convert()
        self.croshair_img.set_colorkey((63,72,204))

        self.bogey_img = image.load(config.BOGEY).convert()
        self.bogey_img.set_colorkey((63,72,204))

        self.missile_img = image.load(config.MISSILE).convert()
        self.missile_img.set_colorkey((63,72,204))

        self.splash_img = image.load(config.SPLASH).convert()
        self.splash_img.set_colorkey((63,72,204))

        self.ship_img = image.load(config.SHIP).convert()
        self.ship_img = transform.scale2x(self.ship_img)
        self.ship_img.set_colorkey((63,72,204))

