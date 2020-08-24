import pygame
import config as config
from pygame import display, event, image, transform, mouse
#from config import config
from time import sleep

clock = pygame.time.Clock()

pygame.init()
display.set_caption('My 2nd PyGame')

SCREEN_SIZE = config.SCREEN_SIZE
BACKGROUND = config.BACKGROUND

screen = display.set_mode(SCREEN_SIZE)

# BACKGROUND
background = image.load(BACKGROUND)
background = transform.scale(background, SCREEN_SIZE)

running = True

while running == True:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.KEYDOWN:
            running = False

        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = mouse.get_pos()

    screen.blit(background,(0,0))

    display.update()
    clock.tick(25)

print('Goodbye!')
