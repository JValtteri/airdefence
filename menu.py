import pygame
from pygame import display, mouse
import game_objects

def menu(screen, clock, images, high_score = 0):
    res = 2
    mode = 1
    menu_text = game_objects.Menutexts()
    in_menu = True

    while in_menu:

        screen.blit( images.background_img, (0,0) )

        menu_text.draw_highscore(screen, high_score)

        res_rect = menu_text.draw_res(screen, res)
        mode_rect = menu_text.draw_mode(screen, mode)
        exit_rect = menu_text.draw_exit(screen)
        start_rect = menu_text.draw_start(screen)


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

            # MOUSE CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = mouse.get_pos()

                if start_rect.collidepoint((mouse_x, mouse_y)):
                    in_menu = False

                elif exit_rect.collidepoint((mouse_x, mouse_y)):
                    in_menu = False
                    mode = 0

                elif res_rect.collidepoint((mouse_x, mouse_y)):
                    print("clicked res")

        display.update()
        clock.tick(15)

    return res, mode