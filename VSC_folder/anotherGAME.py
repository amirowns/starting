# IDLE GAME
# idle fight enemies
    # enemies and user needs hp and stats
# merge stuff to make better equipment
    # figure out click and drag to combine item
    # "lift" item somehow on mouse button down,
    # move the item same pixels that mouse is moving, when mouse button release, \
    #  if item colliding with item of same name, they both dissapeear and a new one pops up
# equip items to user character
    # character needs "slots" to equip items to
    # items also get stats that increase character stats

import sys
import pygame
import Button

# create a clock to track time
clock = pygame.time.Clock()


# color palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
DARK_GRAY = (24, 25, 26)
LIGHT_GRAY = (58, 59, 60)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (40, 255, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 40, 0)

# set up pygame and its screen
pygame.init()
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 800
screen_size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
screen = pygame.display.set_mode(screen_size)

# add window caption
pygame.display.set_caption('Another Idle Game')

# images used
sword_1 = pygame.image.load("VSC_folder/pictures/sword1.png")
sword_1.convert()
sword_rect = sword_1.get_rect()
sword_rect.center = DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2

# set up font and text; size=25, bold=True, italic=False
smallText = pygame.font.SysFont("Arial", 25, True, False)
largeText = pygame.font.SysFont('Arial', 100, True, False)


def game_loop():
    moving = False

    # gets the mouse position
    mouse = pygame.mouse.get_pos()

    # grid starting pos
    MERGE_START_X = DISPLAY_WIDTH * 2/3
    MERGE_START_Y = DISPLAY_HEIGHT * 2/3
    BOX_DIMENSION = 32

    MERGE_BUTTON_LIST = []
    # making buttons
    Button1 = Button.Button(RED, BRIGHT_RED, pygame.Rect(MERGE_START_X, MERGE_START_Y, 32, 32))
    # append buttons to list
    MERGE_BUTTON_LIST.append(Button1)


    while True:
        mouse = pygame.mouse.get_pos()

        # exits game if you click the X in top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if sword_rect.collidepoint(event.pos):
                    moving = True
            elif event.type == pygame.MOUSEMOTION and moving:
                #moves sword relative4 distance mouse moves
                    #sword_rect.move_ip(event.rel)
                # makes the sword center the same as mouse position
                sword_rect.center = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
                # if mouse button release and sword was moving, make the sword rect snap to center of the button
                for button in MERGE_BUTTON_LIST:
                    if button.hovered(mouse):

                        sword_rect.center = button.rect.center
                    

        # fills screen so old swords get covered
        screen.fill(BLACK)

        # bottom half of screen is dark gray
        pygame.draw.rect(screen, DARK_GRAY, (0, DISPLAY_HEIGHT/2, DISPLAY_WIDTH, DISPLAY_HEIGHT/2))

        # buttons
        for button in MERGE_BUTTON_LIST:
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)

        # puts sword on screen
        screen.blit(sword_1, sword_rect)

        # draws border around sword
        pygame.draw.rect(screen, YELLOW, sword_rect, 1, 5)

        # updates stuff on display
        pygame.display.update()


        # limit the update to 60 frames per second
        clock.tick(60)

game_loop()
