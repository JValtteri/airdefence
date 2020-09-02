import pygame
from pygame import display, mouse
import game_objects
from config import full_screen
import webbrowser

def menu(screen, clock, images, config, high_score = 0):
    fps = config.FPS_MODES[0]
    mode = 1
    menu_text = game_objects.Menutexts(config)
    in_menu = True

    while in_menu:

        screen.blit( images.background_img, (0,0) )

        menu_text.draw_highscore(screen, config, high_score)
        credit_rect = menu_text.draw_credits(screen, config)
        res_rect = menu_text.draw_res(screen, config)
        fps_rect = menu_text.draw_fps(screen, config, fps)
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

        elif fps_rect.collidepoint((mouse_x, mouse_y)):
            images.draw_highlite(screen, (fps_rect.midbottom))
            fps_rect = menu_text.draw_fps(screen, config, fps)

        elif res_rect.collidepoint((mouse_x, mouse_y)):
            images.draw_highlite(screen, (res_rect.midbottom))
            res_rect = menu_text.draw_res(screen, config)

        elif credit_rect.collidepoint((mouse_x, mouse_y)):
            images.draw_highlite(screen, (credit_rect.midbottom))
            menu_text.draw_credits(screen, config)

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
                    screen = full_screen(config)

                elif fps_rect.collidepoint((mouse_x, mouse_y)):
                    FPS_MODES = config.FPS_MODES
                    new_mode = (FPS_MODES.index(fps) + 1) % len(FPS_MODES)
                    fps = config.FPS_MODES[new_mode]

                elif credit_rect.collidepoint((mouse_x, mouse_y)):
                    webbrowser.open('https://github.com/JValtteri/airdefence')


        display.update()
        clock.tick(25)

    return fps, mode
