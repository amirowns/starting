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

class Item():
    def __init__(self, image_location):
        self.image_location = image_location
        self.image = pygame.image.load(self.image_location)
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2
        self.moving = False

# images used
sword_1 = Item("VSC_folder/pictures/sword1.png")
shield_1 = Item("VSC_folder/pictures/shield1.png")
sword_2 = Item("VSC_folder/pictures/sword1.png")

# set up font and text; size=25, bold=True, italic=False
smallText = pygame.font.SysFont("Arial", 25, True, False)
largeText = pygame.font.SysFont('Arial', 100, True, False)


def game_loop():

    # gets the mouse position
    mouse = pygame.mouse.get_pos()

    # grid starting pos
    COLUMN_ONE = DISPLAY_WIDTH * 1/4
    ROW_ONE = DISPLAY_HEIGHT * 0.6
    BOX_DIMENSION = 32
    MOVE_OVER = BOX_DIMENSION + 2
    MERGE_BUTTON_LIST = []
    
    # MAKES GRID OF BUTTONS :D
    for x in range(6): # columns
        for y in range(6): # rows
            MERGE_BUTTON_LIST.append(Button.Button(RED, BRIGHT_RED, pygame.Rect((COLUMN_ONE + (x * MOVE_OVER)), (ROW_ONE + (y * MOVE_OVER)), BOX_DIMENSION, BOX_DIMENSION)))

    CURRENT_ITEMS = [] #list of current items in the grid
    CURRENT_ITEMS.append(sword_1)
    CURRENT_ITEMS.append(shield_1)
    CURRENT_ITEMS.append(sword_2)

    CURRENT_ITEM = None

    holding = False
    while True:

        mouse = pygame.mouse.get_pos()
        # fills screen so old swords get covered
        screen.fill(BLACK)

        # bottom half of screen is dark gray
        pygame.draw.rect(screen, DARK_GRAY, (0, DISPLAY_HEIGHT/2, DISPLAY_WIDTH, DISPLAY_HEIGHT/2))

        # buttons
        for button in MERGE_BUTTON_LIST:
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)

        # exits game if you click the X in top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for item in CURRENT_ITEMS:
                    if item.rect.collidepoint(event.pos) and holding == False:
                        item.moving = True
                        CURRENT_ITEM = item
                        CURRENT_ITEMS.remove(item)
                        CURRENT_ITEMS.insert(0, item)
                        print(CURRENT_ITEMS)
                        holding = True
            elif event.type == pygame.MOUSEMOTION:
                for item in CURRENT_ITEMS:
                    if item.moving:
                            #moves sword relative distance mouse moves
                            #sword_rect.move_ip(event.rel)
                        # makes the sword center the same as mouse position
                        item.rect.center = pygame.mouse.get_pos()
                        ###################################################################################### finished changing moving and stuff before ths line
            elif event.type == pygame.MOUSEBUTTONUP:
                if CURRENT_ITEM != None:
                    # if mouse button release and sword was moving, make the sword rect snap to center of the button
                    for button in MERGE_BUTTON_LIST:
                        if button.hovered(mouse) and CURRENT_ITEM.moving:
                            CURRENT_ITEM.rect.center = button.rect.center
                            CURRENT_ITEM.moving = False
                            CURRENT_ITEM = None
                            holding = False

                            # TODO currently moves sword to every button until above if stops the moving in specific button you let go
                            # need to make sword snap back to last button it was on if mouse up not on a box

        # spawns sword on screen, last one drawn gets put on top
        for item in CURRENT_ITEMS[::-1]:
            screen.blit(item.image, item.rect) 

        # draws border around sword
        #pygame.draw.rect(screen, YELLOW, sword_rect, 1, 5)

        # updates stuff on display
        pygame.display.update()


        # limit the update to 60 frames per second
        clock.tick(60)

game_loop()

"""
currently both the sword get picked up at the same time, might pick up all items that are clicked on later lmao.
also need to figure out how to spawn the swords on the next empty button in the grid.
"""