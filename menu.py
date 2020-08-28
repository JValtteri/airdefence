import pygame
from pygame import display, mouse
import game_objects
from config import full_screen

def menu(screen, clock, images, config, high_score = 0):
    res = 2
    mode = 1
    menu_text = game_objects.Menutexts(config)
    in_menu = True

    while in_menu:

        screen.blit( images.background_img, (0,0) )

        menu_text.draw_highscore(screen, config, high_score)
        res_rect = menu_text.draw_res(screen, config)
        # mode_rect = menu_text.draw_mode(screen, config, mode)     # Placeholder for different gamemodes, like accelerating wave
        exit_rect = menu_text.draw_exit(screen, config)
        start_rect = menu_text.draw_start(screen, config)

        # HIGHLITE MOUSEOVER MENU ITEMS
        mouse_x, mouse_y = mouse.get_pos()
        if start_rect.collidepoint((mouse_x, mouse_y)):
            images.draw_highlite(screen, (start_rect.midbottom) )
            menu_text.draw_start(screen, config)

        elif exit_rect.collidepoint((mouse_x, mouse_y)):
            images.draw_highlite(screen, (exit_rect.midbottom))
            menu_text.draw_exit(screen, config)

        elif res_rect.collidepoint((mouse_x, mouse_y)):
            images.draw_highlite(screen, (res_rect.midbottom))
            res_rect = menu_text.draw_res(screen, config)

        # EVENTS
        current_events = pygame.event.get()

        for event in current_events:

            # KEYBOARD
            if event.type == pygame.KEYDOWN:

                # START
                if event.key in (pygame.K_SPACE,
                                pygame.K_RETURN,
                                pygame.K_KP_ENTER
                                ):
                    in_menu = False

                # EXIT
                elif event.key in (pygame.K_ESCAPE,):
                    in_menu = False
                    mode = 0

            # APP CLOSE
            if event.type == pygame.QUIT:
                in_menu = False
                mode = 0

            # MOUSE HOVER

            # MOUSE CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = mouse.get_pos()

                if start_rect.collidepoint((mouse_x, mouse_y)):
                    in_menu = False

                elif exit_rect.collidepoint((mouse_x, mouse_y)):
                    in_menu = False
                    mode = 0

                elif res_rect.collidepoint((mouse_x, mouse_y)):
                    screen = full_screen(config)
                    # print("clicked res")                        # Placeholder for changing rendering resolution or type


        display.update()
        clock.tick(15)

    return res, mode
