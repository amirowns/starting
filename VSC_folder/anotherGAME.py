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
rect = sword_1.get_rect()
rect.center = DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2

# set up font and text; size=25, bold=True, italic=False
smallText = pygame.font.SysFont("Arial", 25, True, False)
largeText = pygame.font.SysFont('Arial', 100, True, False)


def game_loop():
    moving = False
    while True:

        # gets the mouse position
        mouse = pygame.mouse.get_pos()

        # exits game if you click the X in top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving = True
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
            elif event.type == pygame.MOUSEMOTION and moving:
                rect.move_ip(event.rel)
        
        # fills screen so old swords get covered
        screen.fill(BLACK)
        # bottom half of screen is dark gray
        pygame.draw.rect(screen, DARK_GRAY, (0, DISPLAY_HEIGHT/2, DISPLAY_WIDTH, DISPLAY_HEIGHT/2))

        # grid starting pos
        MERGE_START_X = DISPLAY_WIDTH * 2/3
        MERGE_START_Y = DISPLAY_HEIGHT * 2/3

        # Button1 = Button.Button(None, DARK_GRAY, LIGHT_GRAY, None, (MERGE_START_X, MERGE_START_Y, 32, 32))
        # puts sword on screen
        screen.blit(sword_1, rect)

        # draws border around sword
        pygame.draw.rect(screen, YELLOW, rect, 1, 5)

        # updates stuff on display
        pygame.display.update()


        # limit the update to 60 frames per second
        clock.tick(60)

game_loop()
