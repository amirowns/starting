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
from threading import Timer
import Button
from random import choice
import json
import entities
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
screen_rect = screen.get_rect()

# add window caption
pygame.display.set_caption('Another Idle Game')
    
current_items_list = [] #list of current items in the grid
MERGE_BUTTON_LIST = []
SCREEN_BUTTON_LIST = []
player_stats_button_list = []
# set up font and text; size=25, bold=True, italic=False
smallText = pygame.font.SysFont("Arial", 10, True, False)
medText = pygame.font.SysFont('Arial', 25, True, False)
largeText = pygame.font.SysFont('Arial', 100, True, False)

def create_text(x, y, font, text, text_color, background_color=None):
    text_surface = font.render(text, False, text_color, background_color)
    screen.blit(text_surface, (x, y))

class Item():
    def __init__(self, item_type, item_level, image_location):
        self.item_type = item_type
        self.item_level = item_level
        self.image_location = image_location
        self.image = pygame.image.load(self.image_location)
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2
        self.moving = False

    def __str__(self):
        return f"level {self.item_level} {self.item_type}, rect = {self.rect}, moving? {self.moving}."

def saveItems():
    json_string = json.dumps([(item.item_type, item.item_level, item.image_location) for item in current_items_list])
    print(json_string)
    with open("Save_file.json", "w") as f:
        f.write(json_string)

def loadItems():
    with open("Save_file.json", "r") as f:
        itemStats = json.load(f)
        for item in itemStats:
            current_items_list.append(Item(item[0], item[1], item[2]))

def drop_table():
    for button in MERGE_BUTTON_LIST:
        if button.has_item == False:
            RNGesus = choice(range(1, 10))
            if RNGesus >1:
                if RNGesus >5:
                    new_drop = Item("sword", 1, "VSC_folder/pictures/sword1.png")
                    current_items_list.append(new_drop) # make a new lvl 1 sword

                elif RNGesus >1:
                    new_drop = Item("shield", 1, "VSC_folder/pictures/shield1.png")
                    current_items_list.append(new_drop) # make a new lvl 1 shield
            else:
                new_drop = None 
            if new_drop != None:
                for button in MERGE_BUTTON_LIST:
                    if button.has_item == False:
                        new_drop.rect.center = button.rect.center
                        button.has_item = True
                        break
            break

def merge_item():
    pass

def starting_items():
    # starting items
    current_items_list.append(Item("sword", 1, "VSC_folder/pictures/sword1.png"))
    current_items_list.append(Item("shield", 1, "VSC_folder/pictures/shield1.png"))

def blit_text(what):
    textSurf, textRect = what.text_objects
    textRect.center = (what.rect.center)
    screen.blit(textSurf, textRect)

def attack_other(attacker, defender):
    if attacker.attack > defender.defense:
        defender.current_health -= (attacker.attack - defender.defense)  

def hovered_by_mouse(thing_being_hovered):
    mouse = pygame.mouse.get_pos()
    return thing_being_hovered.rect.collidepoint(mouse)

def game_intro():

    intro = True

    MM_Button_list = []
    screen.fill(BLACK)
    #message_display("Idle Game")

    # make buttons and add them to MM_Button_list
    MM_Button_list.append(Button.TTTButton("New Game", GREEN, BRIGHT_GREEN, medText, pygame.Rect(DISPLAY_WIDTH * 0.4, DISPLAY_HEIGHT * .35, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1)))
    MM_Button_list.append(Button.TTTButton("Continue", GREEN, BRIGHT_GREEN, medText, pygame.Rect(DISPLAY_WIDTH * 0.4, DISPLAY_HEIGHT * .55, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1)))
    MM_Button_list.append(Button.TTTButton("Quit", RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0.4, DISPLAY_HEIGHT * .75, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1)))

    while intro:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in MM_Button_list:
                    if hovered_by_mouse(button):
                        if button.text == "New Game":
                            # open new game file
                            starting_items()
                            game_loop()
                        elif button.text == "Continue":
                            # open the save file
                            loadItems()
                            game_loop()
                        elif button.text == "Quit":
                            sys.exit()    
            else: 
                pass
        # "runs" the buttons
        for button in MM_Button_list:
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)
            blit_text(button)

        pygame.display.update()
        clock.tick(15)
################################################################################################################
def game_loop():
    # gets the mouse position
    mouse = pygame.mouse.get_pos()
    timer = 0
    # grid starting pos
    COLUMN_ONE = DISPLAY_WIDTH * 1/4
    ROW_ONE = DISPLAY_HEIGHT * 0.6
    BOX_DIMENSION = 32
    MOVE_OVER = BOX_DIMENSION + 2
    
    # MAKES GRID OF BUTTONS :D
    for y in range(6): # columns
        for x in range(6): # rows
            MERGE_BUTTON_LIST.append(Button.Button(RED, BRIGHT_RED, pygame.Rect((COLUMN_ONE + (x * MOVE_OVER)), (ROW_ONE + (y * MOVE_OVER)), BOX_DIMENSION, BOX_DIMENSION)))
    
    SCREEN_BUTTON_LIST.append(Button.TTTButton("Sort", RED, BRIGHT_RED, medText, pygame.Rect(COLUMN_ONE, ROW_ONE + (7 * MOVE_OVER), BOX_DIMENSION * 2, BOX_DIMENSION)))
    
    # makes the player object with stats
    player = entities.Player()
    goblin = entities.Goblin()

    current_enemy = goblin
    
    # makes player stat buttons and adds em to list
    # could potentially make normal button for hp, and another button for the text of hp so the text doesnt move
    player_health = Button.TTTButton(f"HP: {player.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(player.rect.x, player.rect.top - 30, (player.current_health / player.max_health * player.rect.width), 20))
    player_stats_button_list.append(player_health)
    player_attack = Button.TTTButton(f"ATK: {player.attack}", LIGHT_GRAY, LIGHT_GRAY, smallText, pygame.Rect(player.rect.x, player.rect.bottom + 10, player.rect.width, 20))
    player_stats_button_list.append(player_attack)
    player_defense = Button.TTTButton(f"DEF: {player.defense}", LIGHT_GRAY, LIGHT_GRAY, smallText, pygame.Rect(player.rect.x, player.rect.bottom + 10 + 30, player.rect.width, 20))
    player_stats_button_list.append(player_defense)

    # enemy stats
    enemy_health = Button.TTTButton(f"HP: {current_enemy.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(current_enemy.rect.x, current_enemy.rect.top - 30, (current_enemy.current_health / current_enemy.max_health * current_enemy.rect.width), 20))
    """
    for button in player_stats_button_list:
        pygame.draw.rect(screen, YELLOW, button.rect, 1)
    """
    current_item = None
    switched_item = None
    holding = False
    counter = 0
    # if button is not full, spawn item at button location and make button have item
    for item in current_items_list:
        for button in MERGE_BUTTON_LIST:
            if button.has_item == False:
                item.rect.center = button.rect.center
                button.has_item = True
                break

    
    ############################################################################################################
    while True:

        mouse = pygame.mouse.get_pos()
        # fills screen so old swords get covered
        screen.fill(DARK_GRAY)

        # bottom half of screen is dark gray
        #pygame.draw.rect(screen, DARK_GRAY, (0, DISPLAY_HEIGHT/2, DISPLAY_WIDTH, DISPLAY_HEIGHT/2))

        # buttons
        for button in MERGE_BUTTON_LIST:
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)
            pygame.draw.rect(screen, BLACK, button.rect, 1)

        for button in SCREEN_BUTTON_LIST:
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)
            blit_text(button)

        # exits game if you click the X in top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saveItems()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    for item in current_items_list:
                        if item.rect.collidepoint(event.pos) and holding == False:
                            holding = True
                            item.moving = True
                            current_item = item # makes the item you click the current item
                            # makes item clicked go to front of the list
                            current_items_list.remove(item)
                            current_items_list.insert(0, item)
                            position_on_mousedown = item.rect.center
                            # for gtting button on mousedown
                            for button in MERGE_BUTTON_LIST:
                                if hovered_by_mouse(button):
                                    button_on_mousedown = MERGE_BUTTON_LIST.index(button) # gets the index of button clicked on 

                elif event.button == 3: # right click
                    drop_table()

                elif event.button ==2: # middle mouse button
                    if player.current_health > 0:
                        attack_other(player, current_enemy)
                        enemy_health = Button.TTTButton(f"HP: {current_enemy.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(current_enemy.rect.x, current_enemy.rect.top - 30, (current_enemy.current_health / current_enemy.max_health * current_enemy.rect.width), 20))
                        if current_enemy.current_health > 0:
                            attack_other(current_enemy, player)
                            player_stats_button_list.remove(player_health)
                            player_health = Button.TTTButton(f"HP: {player.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(player.rect.x, player.rect.top - 30, (player.current_health / player.max_health * player.rect.width), 20))
                            player_stats_button_list.append(player_health)
                        elif current_enemy.current_health <= 0:
                            drop_table()
                            counter += 1
                            print(counter)
                            current_enemy.current_health = current_enemy.max_health
                            enemy_health = Button.TTTButton(f"HP: {current_enemy.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(current_enemy.rect.x, current_enemy.rect.top - 30, (current_enemy.current_health / current_enemy.max_health * current_enemy.rect.width), 20))
                    elif player.current_health <= 0:
                        counter = 0

                        current_enemy.current_health = current_enemy.max_health
                        enemy_health = Button.TTTButton(f"HP: {current_enemy.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(current_enemy.rect.x, current_enemy.rect.top - 30, (current_enemy.current_health / current_enemy.max_health * current_enemy.rect.width), 20))
                        
                        player_stats_button_list.remove(player_health)
                        player.current_health = player.max_health
                        player_health = Button.TTTButton(f"HP: {player.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(player.rect.x, player.rect.top - 30, (player.current_health / player.max_health * player.rect.width), 20))
                        player_stats_button_list.append(player_health)
                        
            elif event.type == pygame.MOUSEMOTION:
                for item in current_items_list:
                    if item.moving:
                            #moves sword relative distance mouse moves
                            #sword_rect.move_ip(event.rel)
                        # makes the sword center the same as mouse position
                        item.rect.center = pygame.mouse.get_pos()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # left click
                    if current_item != None: # if there is an item clicked 
                        holding = False # an item isn't being held anymore
                        #current_item.rect.center = position_on_mousedown # the item goes back to where you picked it up
                        position_i_want = position_on_mousedown # defaults position i want to where i picked it up
                        for button in MERGE_BUTTON_LIST: # check every button
                            if hovered_by_mouse(button) and current_item.moving: # to see if the button is hovered, there's an item moving
                                position_i_want = button.rect.center # updates position i want to the button position
                                if button.has_item == False: # if the button is empty
                                    button.has_item = True # say the button has_item
                                elif button.has_item == True: # if the button has an item
                                    for item in current_items_list: # check every item
                                        if item.rect.center == button.rect.center: # if the item location is the same as the hovered button location
                                            switched_item = item # make that item the switched item
                                            switched_item.rect.center = MERGE_BUTTON_LIST[button_on_mousedown].rect.center # and move that item to the mousedown location
                        current_item.rect.center = position_i_want  # moves the item to the position i want 

                        # currently breaks if items dont start on a button
                        if current_item.rect.center != position_on_mousedown and switched_item == None:  # if item position isnt same as when it was picked up and not switching items
                            try:
                                MERGE_BUTTON_LIST[button_on_mousedown].has_item = False # say the button it was on before doesn't have item anymore
                            except:
                                pass
                        
                        current_item.moving = False 
                        # if both the items are the same type and level, delete both of them, and make an item of level+1
                        if current_item != None and switched_item != None and current_item != switched_item:
                            if current_item.item_type == switched_item.item_type and current_item.item_level == switched_item.item_level:
                                try: # if new item of level+1 exists
                                    new_item = Item(current_item.item_type, current_item.item_level + 1, f"VSC_folder/pictures/{current_item.item_type}{current_item.item_level + 1}.png")
                                    new_item.rect.center = current_item.rect.center
                                    current_items_list.append(new_item) # make new item level+1
                                    current_items_list.remove(current_item)
                                    current_items_list.remove(switched_item)
                                    MERGE_BUTTON_LIST[button_on_mousedown].has_item = False
                                except: # otherwise:
                                    print(f"Sorry, I haven't made a level {current_item.item_level + 1} {current_item.item_type} yet :(")

                        current_item = None
                        switched_item = None

                    for button in SCREEN_BUTTON_LIST:
                        if hovered_by_mouse(button):
                            current_items_list.sort(key = lambda x: x.item_level, reverse = True) # sort by highest item level first
                            current_items_list.sort(key = lambda x: x.item_type) # sort by type of item
                            # need to move items to correct locations now

                            for button in MERGE_BUTTON_LIST:
                                button.has_item = False

                            for item in current_items_list:
                                for button in MERGE_BUTTON_LIST:
                                    if button.has_item == False:
                                        item.rect.center = button.rect.center
                                        button.has_item = True
                                        break
        


        if pygame.time.get_ticks() - timer> 1500:
            timer = pygame.time.get_ticks()
            if player.current_health > 0:
                attack_other(player, current_enemy)
                enemy_health = Button.TTTButton(f"HP: {current_enemy.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(current_enemy.rect.x, current_enemy.rect.top - 30, (current_enemy.current_health / current_enemy.max_health * current_enemy.rect.width), 20))
                if current_enemy.current_health > 0:
                    attack_other(current_enemy, player)
                    player_stats_button_list.remove(player_health)
                    player_health = Button.TTTButton(f"HP: {player.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(player.rect.x, player.rect.top - 30, (player.current_health / player.max_health * player.rect.width), 20))
                    player_stats_button_list.append(player_health)
                elif current_enemy.current_health <= 0:
                    drop_table()
                    counter += 1
                    print(counter)
                    current_enemy.current_health = current_enemy.max_health
                    enemy_health = Button.TTTButton(f"HP: {current_enemy.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(current_enemy.rect.x, current_enemy.rect.top - 30, (current_enemy.current_health / current_enemy.max_health * current_enemy.rect.width), 20))
            elif player.current_health <= 0:
                counter = 0

                current_enemy.current_health = current_enemy.max_health
                enemy_health = Button.TTTButton(f"HP: {current_enemy.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(current_enemy.rect.x, current_enemy.rect.top - 30, (current_enemy.current_health / current_enemy.max_health * current_enemy.rect.width), 20))
                
                player_stats_button_list.remove(player_health)
                player.current_health = player.max_health
                player_health = Button.TTTButton(f"HP: {player.current_health}", BRIGHT_RED, BRIGHT_RED, smallText, pygame.Rect(player.rect.x, player.rect.top - 30, (player.current_health / player.max_health * player.rect.width), 20))
                player_stats_button_list.append(player_health)

        # draws the player and enemy
        screen.blit(player.image, player.rect)
        screen.blit(current_enemy.image, current_enemy.rect)

        # draws goblin hp bar
        pygame.draw.rect(screen, enemy_health.current_color, enemy_health.rect)
        blit_text(enemy_health)

        # draws player stat buttons
        for button in player_stats_button_list:
            pygame.draw.rect(screen, button.current_color, button.rect)
            blit_text(button)

        # max hp bar outline doesnt move
        pygame.draw.rect(screen, YELLOW, (player.rect.x, player.rect.top - 30, player.rect.width, 20), 1)
        pygame.draw.rect(screen, YELLOW, (current_enemy.rect.x, current_enemy.rect.top - 30, current_enemy.rect.width, 20), 1)

        # spawns sword on screen, last one drawn gets put on top
        for item in current_items_list[::-1]:
            screen.blit(item.image, item.rect)
            create_text(item.rect.x + 2, item.rect.y, smallText, f'{item.item_level}', WHITE, BLACK)

        # updates stuff on display
        pygame.display.update()

        # limit the update to 60 frames per second
        clock.tick(60)

game_intro()

"""
TODO 
SQL DATABASES? JSON FOR STORING PLAYER DATA? FOR SAVE/LOAD FILES :D
character class and stats
character inventory and equip items screen to raise stats

"""