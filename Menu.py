import pygame
import sys
import Helper
from pygame.locals import *

pygame.init()
FPS = 60
FPS_CLOCK = pygame.time.Clock()
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE
pygame.display.set_caption('Sekai Saviour')

BLACK = (0, 0, 0)                # currently used for the background
BACKGROUND_GOLD = (124, 91, 51)   # currently unused
BUTTON_GOLD = (147, 117, 53)      # colour of the buttons
HIGHLIGHT = (150, 120, 100, 20)  # colour of the highlight

buttons = dict(
    buttonNewGame=pygame.Rect(50, 434, 300, 150),  # TODO lower the buttons
    buttonContinue=pygame.Rect(400, 434, 300, 150),
    buttonSettings=pygame.Rect(50, 634, 300, 150),
    buttonQuit=pygame.Rect(400, 634, 300, 150),
    settingsBackground=pygame.Rect(25, 375, 700, 600),
    settingsExit=pygame.Rect(50, 900, 100, 50)
    )


def draw_menu():  # Draws rectangles to represent the 'buttons'
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttons['buttonNewGame'])
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttons['buttonContinue'])
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttons['buttonSettings'])
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttons['buttonQuit'])


def draw_settings_menu():
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttons['settingsBackground'])
    pygame.draw.rect(DISPLAY_SURFACE, BACKGROUND_GOLD, buttons['settingsExit'])


def check_buttons(click_pos):  # TODO change these to elifs
    """
    Checks which 'button' was clicked,
    can assign functions to each separate button
    Arguments:
        click_pos -- position of the mouse click
    """
    if buttons['buttonQuit'].collidepoint(click_pos):
        print("Button clicked: Quit")
        return 'Quit'

    elif buttons['buttonNewGame'].collidepoint(click_pos):
        print("Button clicked: New Game")
        return 'New_Game'

    elif buttons['buttonContinue'].collidepoint(click_pos):
        print("Button clicked: Continue")
        # return 'Continue'

    elif buttons['buttonSettings'].collidepoint(click_pos):
        print("Button clicked: Settings")
        return 'Settings'

    elif buttons['settingsExit'].collidepoint(click_pos):
        print("Button clicked: Exit Settings")
        return 'Main_Menu'

    return 'Main_Menu'


def highlight_buttons(mx, my):  # Draws a highlight over a button on mouse-over
    if buttons['buttonNewGame'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonNewGame'])
    if buttons['buttonContinue'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonContinue'])
    if buttons['buttonSettings'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonSettings'])
    if buttons['buttonQuit'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonQuit'])
    if buttons['settingsExit'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['settingsExit'])


def menu_update():
    (mouse_x, mouse_y) = (0, 0)
    while True:
        DISPLAY_SURFACE.fill(BLACK)
        draw_menu()

        for event in pygame.event.get():
            # stores most recent mouse movement in two variables
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_f:  # TODO remove this code
                    return 'New_Game'

            # check if a button was clicked on mouse click
            elif event.type == MOUSEBUTTONUP:
                click_pos = pygame.mouse.get_pos()
                return check_buttons(click_pos)

        highlight_buttons(mouse_x, mouse_y)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def settings_menu_update():
    (mouse_x, mouse_y) = (0, 0)
    while True:
        DISPLAY_SURFACE.fill(BLACK)
        draw_settings_menu()

        for event in pygame.event.get():
            # stores most recent mouse movement in two variables
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_f:  # TODO remove this code
                    return 'New_Game'

            # check if a button was clicked on mouse click
            elif event.type == MOUSEBUTTONUP:
                click_pos = pygame.mouse.get_pos()
                return check_buttons(click_pos)

        highlight_buttons(mouse_x, mouse_y)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
