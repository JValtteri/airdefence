import pygame
from pygame import display, mouse
import random
from config import Config, init_screen
import game_objects
import menu
from game_objects import Images, Texts

# INIT

# Load config
config = Config()
screen = init_screen(config)
clock = pygame.time.Clock()
images = Images(config)
texts = Texts(config)


# CONFIG
SCREEN_SIZE = config.SCREEN_SIZE
ASSET_SIZE = config.ASSET_SIZE
SHIP_LOCALE = config.SHIP_LOCALE


# FUNCTIONS

def vector(end, start=(0, 0) ):
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]

    return (delta_x, delta_y)


def splash_it(missile, bogey):
    missile.splash(images.splash_img)
    missile.speed(0)
    missile.show(20)
    missile.expire = True

    bogey.speed(0)
    bogey.show(5)
    bogey.expire = True


def check_collision(bogeys, missiles):
    hits = 0
    for bogey in bogeys:
        for missile in missiles:
            if missile.rect.colliderect(bogey.rect) and missile.image is not images.splash_img:
                splash_it(missile, bogey)
                hits += 1
    return hits


def is_garbage(item):
    return item.expire == True and item.time == 0


def refill_clip(clip):
    if clip < 4:
        clip += 1
    return clip


# SPAWNERS

def spawn_bogey(x, v=10):
    bogey = game_objects.Object(images.bogey_img, x, v=v)
    bogey.show(375)
    return bogey


def spawn_missile(vect, v=20):
    missile = game_objects.Object(
                     image = images.missile_img,
                     x = SHIP_LOCALE[0],
                     y = SHIP_LOCALE[1],
                     v = v,
                     vect = vect)
    missile.show(300)
    return missile


def play():

    # OBJECTS
    croshair = game_objects.Object(images.croshair_img)
    bogeys = []
    missiles = []
    clip = 4
    score = 0
    missed = 0
    lives = 3
    ship = game_objects.Object(
                image=images.ship_img,
                x = SHIP_LOCALE[0],
                y = SHIP_LOCALE[1],
                expire = False
                )

    # ship_rect = config.ship_img.get_rect(center = (SHIP_LOCALE))
    ship.show(-1)


    # EVENTS
    SPAWNBOGEY = pygame.USEREVENT
    pygame.time.set_timer(SPAWNBOGEY,800)  # Start 1500

    REFILL = pygame.USEREVENT + 1
    pygame.time.set_timer(REFILL,700)


    running = True


    # GAME LOOP

    while running == True:

        # GARBAGE COLLECTION
        #
        # deletes objects that have expired:
        # whose time has run out and expiration is enabled
        missiles = [missile for missile in missiles if not is_garbage(missile)]
        bogeys = [bogey for bogey in bogeys if not is_garbage(bogey)]


        # DRAWING
        screen.blit( images.background_img, (0,0) )
        ship.draw(screen)
        croshair.draw(screen)
        texts.clip_display(screen, config, clip)
        texts.score_display(screen, config, score)
        texts.debug_display(screen, config, missiles, bogeys)

        # Draw Bogeys
        for bogey in bogeys:
            bogey.move_y()
            bogey.draw(screen)
            # Check if Bogey is leaving the screen
            if bogey.rect.centery > SCREEN_SIZE[1]:
                missed += 1
                bogey.show(0)

        # Draw Missiles
        for missile in missiles:
            missile.move_2d()
            missile.draw(screen)

        # Check collisions
        hits = check_collision(bogeys, missiles)
        score += hits

        # If enough bogeys aren't shot down
        # end the game
        if missed >= lives:
            running = False

        # EVENTS
        current_events = pygame.event.get()
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
                                        random.randrange(32, SCREEN_SIZE[0]-32),
                                        random.randrange(5, 15)
                                        ))

            if event.type == REFILL:
                clip = refill_clip(clip)

        display.update()
        clock.tick(25)


    # SHOW POST_GAME


    post_game = True

    while post_game:

        # screen.blit( background_img, (0,0) )
        texts.clip_display(screen, config, clip)
        texts.score_display(screen, config, score)
        texts.debug_display(screen, config, missiles, bogeys)
        texts.gameover_display(screen, config, score)

        current_events = pygame.event.get()
        for event in current_events:

            # KEYBOARD
            if event.type == pygame.KEYDOWN:

                post_game = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     post_game = False

            # APP CLOSE
            if event.type == pygame.QUIT:
                post_game = False


        display.update()
        clock.tick(5)

    return score


if __name__ == "__main__":
    high_score = 0
    mode = 1
    while mode > 0:
        resolution, mode = menu.menu(screen, clock, images, config, high_score)
        if mode > 0:
            score = play()
            if score > high_score:
                high_score = score
