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
    for x in range(3): # columns
        for y in range(3): # rows
            MERGE_BUTTON_LIST.append(Button.Button(RED, BRIGHT_RED, pygame.Rect((COLUMN_ONE + (x * MOVE_OVER)), (ROW_ONE + (y * MOVE_OVER)), BOX_DIMENSION, BOX_DIMENSION)))

    current_items_list = [] #list of current items in the grid
    current_items_list.append(sword_1)
    current_items_list.append(shield_1)
    current_items_list.append(sword_2)

    current_item = None

    holding = False
    #############################################################################################
    # currently spawns items in to last button 
    for item in current_items_list:
        for button in MERGE_BUTTON_LIST:
            if button.has_item == False:
                item.rect.center = button.rect.center
    ############################################################################################################
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
                for item in current_items_list:
                    if item.rect.collidepoint(event.pos) and holding == False:
                        item.moving = True
                        current_item = item # makes the item you click the current item
                        # makes item clicked go to front of the list
                        current_items_list.remove(item)
                        current_items_list.insert(0, item)
                        holding = True
                        position_on_mousedown = item.rect.center
                        ################################################################
                        for button in MERGE_BUTTON_LIST:
                            if button.hovered(mouse):
                                button_on_mousedown = MERGE_BUTTON_LIST.index(button) # gets the index of button clicked on 
                                print(button_on_mousedown)
                        #################################################################
                        
            elif event.type == pygame.MOUSEMOTION:
                for item in current_items_list:
                    if item.moving:
                            #moves sword relative distance mouse moves
                            #sword_rect.move_ip(event.rel)
                        # makes the sword center the same as mouse position
                        item.rect.center = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if current_item != None: # if there is an item clicked 
                    current_item.rect.center = position_on_mousedown # the item goes back to where you picked it up
                    position_i_want = position_on_mousedown # defaults position i want to where i picked it up
                    holding = False # an item isn't being held anymore
                    for button in MERGE_BUTTON_LIST: # check every button
                        if button.hovered(mouse) and current_item.moving and button.has_item == False: # to see if the button is hovered, there's an item moving, and the button has_item
                            position_i_want = button.rect.center # updates position i want to the button position
                            holding = False # nothing is being held anymore
                            button.has_item = True # say the button has_item
                    current_item.rect.center = position_i_want  # moves the item to the position i want 
                    ################################################################## 
                    # currently breaks if items dont start on a button
                    if current_item.rect.center != position_on_mousedown:  # if item position isnt same as when it was picked up
                        MERGE_BUTTON_LIST[button_on_mousedown].has_item = False # say the button it was on before doesn't have item anymore

                    for button in MERGE_BUTTON_LIST: #testing
                        print(button.has_item) #testing
                    ##################################################################    
                    current_item.moving = False 
                    current_item = None
        # spawns sword on screen, last one drawn gets put on top
        for item in current_items_list[::-1]:
            screen.blit(item.image, item.rect) 

        # draws border around sword
        #pygame.draw.rect(screen, YELLOW, sword_rect, 1, 5)

        # updates stuff on display
        pygame.display.update()


        # limit the update to 60 frames per second
        clock.tick(60)

game_loop()

"""
TODO need to make only 1 item per button
    need to make it so when item is moving and button up outside of button, item snaps back where it was
    make it so if one item is dragged on top of another item, they swap places
    make it so two of same item dragged on top of eachother get deleted and new item of lvl+1 appears
"""