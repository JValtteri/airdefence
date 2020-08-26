import math
from pygame import image, transform
# import config

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

    def __init__(self, config):

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


class Texts():

    def __init__(self, config):
        self.game_font = config.get_fonts()

    def clip_display(self, screen, config, clip):
        score_surface = self.game_font.render('Missiles: {}'.format(clip), True, (225,225,225) )
        score_rect = score_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2 - 200, config.SCREEN_SIZE[1] - 70 ) )
        screen.blit(score_surface, score_rect)

    def score_display(self, screen, config, score):
        score_surface = self.game_font.render('Score: {}'.format(score), True, (225,225,225) )
        score_rect = score_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2 + 200, config.SCREEN_SIZE[1] - 70 ) )
        screen.blit(score_surface, score_rect)

    def debug_display(self, screen, config, missiles, bogeys):
        score_surface = self.game_font.render('M: {} B:{}'.format( len(missiles), len(bogeys) ), True, (225,225,225) )
        score_rect = score_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2,  70 ) )
        screen.blit(score_surface, score_rect)

    def gameover_display(self, screen, config, score):
        lines = ['GAME OVER', 'Score: {}'.format(score)]
        for i in range(len(lines)):
            gameover_surface = self.game_font.render(lines[i], True, (225,225,225) )
            gameover_rect = gameover_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2,  config.SCREEN_SIZE[1] / 2 + 44 * i ) )
            screen.blit(gameover_surface, gameover_rect)


class Menutexts():

    def __init__(self, config):
        self.menu_font = config.get_fonts()

    def draw_highscore(self, screen, config, highs_core):
        highscore_surface = self.menu_font.render('Highscore: {}'.format(highs_core), True, (225,225,225) )
        highscore_rect = highscore_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2,  70 ) )
        screen.blit(highscore_surface, highscore_rect)

    def draw_res(self, screen, config):
        res_surface = self.menu_font.render('{} x {}'.format(config.SCREEN_SIZE[0], config.SCREEN_SIZE[1]), True, (225,225,225) )
        res_rect = res_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2,  config.SCREEN_SIZE[1] / 2 - 44 ) )
        screen.blit(res_surface, res_rect)
        return res_rect

    def draw_mode(self, screen, config, mode):
        mode_surface = self.menu_font.render('{}'.format(mode), True, (225,225,225) )
        mode_rect = mode_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2,  config.SCREEN_SIZE[1] / 2 + 44 ) )
        screen.blit(mode_surface, mode_rect)
        return mode_rect

    def draw_exit(self, screen, config):
        exit_surface = self.menu_font.render('Exit', True, (225,225,225) )
        exit_rect = exit_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2 + 200, config.SCREEN_SIZE[1] - 70 ) )
        screen.blit(exit_surface, exit_rect)
        return exit_rect

    def draw_start(self, screen, config):
        start_surface = self.menu_font.render('START', True, (225,225,225) )
        start_rect = start_surface.get_rect(center = (config.SCREEN_SIZE[0] / 2, config.SCREEN_SIZE[1] - 70 ) )
        screen.blit(start_surface, start_rect)
        return start_rect




