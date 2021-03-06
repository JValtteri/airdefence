import pygame

class Config():

    FONT = 'assets/04B_19.TTF'

    def __init__(self):

        # self.SCREEN_SIZES = ((600, 480),  (1024, 700),    (1024,1024),    (2048, 1340) )
        # self.ASSET_SIZES = ( (24, 24),    (32, 32),       (64, 64),       (86, 86) )
        self.SCREEN_SIZE = [1024,1024]      # monitor_info.current_h-60
        self.ASSET_SIZE = (64, 64)
        self.FPS_MODES = (60, 120, 25, 50)
        self.BACKGROUND = 'assets/bg.png'
        self.CROSHAIR = 'assets/croshair.png'
        self.BOGEY = 'assets/plane-red.png'
        self.MISSILE = 'assets/missile.png'
        self.SPLASH = 'assets/splash.png'
        self.SHIP = 'assets/ship.png'
        self.HIGHLITE = 'assets/highlite.png'
        self.HIGH_SCORE = 0
        self.SHIP_LOCALE = ( self.SCREEN_SIZE[0] / 2, self.SCREEN_SIZE[1] - 100 )
        self.GAME_FONT = None

    def get_fonts(self, index=0):
        if index == 0:
            afont = pygame.font.Font(Config.FONT, 40)
        elif index == 1:
            afont = pygame.font.Font(Config.FONT, 20)
        return afont

    def update_screen_size(self, new_screen_y):
        self.SCREEN_SIZE[1] = new_screen_y
        self.SHIP_LOCALE = ( self.SCREEN_SIZE[0] / 2, self.SCREEN_SIZE[1] - 100 )

def init_screen(config):
    pygame.init()
    monitor_info = pygame.display.Info()
    if monitor_info.current_h < 2024:
        config.update_screen_size(monitor_info.current_h - 70)
    screen = pygame.display.set_mode((config.SCREEN_SIZE))#, pygame.FULLSCREEN)
    pygame.display.set_caption('Air Defence')
    return screen

def full_screen(config):
    pygame.init()
    monitor_info = pygame.display.Info()
    if monitor_info.current_h < 2024:
        print(monitor_info.current_h)                       # DEBUG
        config.update_screen_size(monitor_info.current_h)
    screen = pygame.display.set_mode((config.SCREEN_SIZE ), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)#, pygame.FULLSCREEN)
    return screen
