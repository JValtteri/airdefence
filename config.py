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
    monitor_info = pygame.display.Info()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_SIZE[0], monitor_info.current_h-60))#, pygame.FULLSCREEN)
    pygame.display.set_caption('Air defence')

    return screen, clock, monitor_info.current_h

def get_fonts():
    game_font = pygame.font.Font(FONT, 40)
    return game_font
