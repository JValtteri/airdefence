import pygame

# IMAGE_SIZE = 128
SCREEN_SIZES = ((600, 480),  (1024, 700),    (1024,1024),    (2048, 1340) )
ASSET_SIZES = ( (24, 24),    (32, 32),       (64, 64),       (86, 86) )
SCREEN_SIZE = (1024,1024)
ASSET_SIZE = (64, 64)
BACKGROUND = 'assets/bg.png'
CROSHAIR = 'assets/croshair.png'
BOGEY = 'assets/plane-red.png'
MISSILE = 'assets/missile.png'
SPLASH = 'assets/splash.png'
SHIP = 'assets/ship.png'
FONT = 'assets/04B_19.TTF'
HIGH_SCORE = 0

SHIP_LOCALE = ( SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - 100 )

def init_screen():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Air defence')

    return screen, clock

def get_fonts():
    game_font = pygame.font.Font(FONT, 40)
    return game_font