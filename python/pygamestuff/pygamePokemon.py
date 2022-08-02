import sys
import pygame
import Button
from SQLconnectiontest import Pokemon
from SQLconnectiontest import TypeEffectiveness
from pokemonParty import Party
from random import choice

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

pokecolors = {
"Normal" : pygame.Color('#A8A77A'),
"Fire" : pygame.Color('#EE8130'),
"Water" : pygame.Color('#6390F0'),
"Electric" : pygame.Color('#F7D02C'),
"Grass" : pygame.Color('#7AC74C'),
"Ice" : pygame.Color('#96D9D6'),
"Fighting" : pygame.Color('#C22E28'),
"Poison" : pygame.Color('#A33EA1'),
"Ground" : pygame.Color('#E2BF65'),
"Flying" : pygame.Color('#A98FF3'),
"Psychic" : pygame.Color('#F95587'),
"Bug" : pygame.Color('#A6B91A'),
"Rock" : pygame.Color('#B6A136'),
"Ghost" : pygame.Color('#735797'),
"Dragon" : pygame.Color('#6F35FC'),
"Dark" : pygame.Color('#705746'),
"Steel" : pygame.Color('#B7B7CE'),
"Fairy" : pygame.Color('#D685AD'),
}
# set up pygame and its screen
pygame.init()
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 800
screen_size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
screen = pygame.display.set_mode(screen_size)
screen_rect = screen.get_rect()

# create a clock to track time
clock = pygame.time.Clock()

# add window caption
pygame.display.set_caption('Pokemon??')

# set up font and text; size=25, bold=True, italic=False
smallText = pygame.font.SysFont("Arial", 10, True, False)
medText = pygame.font.SysFont('Arial', 25, True, False)
largeText = pygame.font.SysFont('Arial', 100, True, False)

# only allows certain events
pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONUP])

length = DISPLAY_WIDTH * 0.4
height = DISPLAY_HEIGHT * 0.1

wait_time = 0
went = False
move_chosen = False


def create_text(x, y, font, text, text_color, background_color=None, centered=False):
    text_surface = font.render(text, False, text_color, background_color)
    if centered == False:
        screen.blit(text_surface, (x, y))
    else:
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)       

def blit_text(what):
    textSurf, textRect = what.text_objects
    textRect.center = (what.rect.center)
    screen.blit(textSurf, textRect)

def hovered_by_mouse(thing_being_hovered):
    mouse = pygame.mouse.get_pos()
    return thing_being_hovered.rect.collidepoint(mouse)
    

def game_intro():

    intro = True
    MM_Button_list = []

    # make buttons and add them to MM_Button_list
    MM_Button_list.append(Button.TTTButton("Battle", GREEN, BRIGHT_GREEN, medText, pygame.Rect(DISPLAY_WIDTH * 0.4, DISPLAY_HEIGHT * .35, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1)))
    MM_Button_list.append(Button.TTTButton("Quit", RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0.4, DISPLAY_HEIGHT * .55, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1)))

    while intro:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in MM_Button_list:
                    if hovered_by_mouse(button):
                        if button.text == "Battle":
                            #intro = False
                            Random_battle()
                        elif button.text == "Quit":
                            sys.exit()
        # "runs" the buttons
        for button in MM_Button_list:
            mouse = pygame.mouse.get_pos()
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)
            blit_text(button)

        pygame.display.update()
        clock.tick(15)

def Random_battle():
    Buttonmovelist = []
    Pokemonlist = []
    Battlemenulist = []
    MenuButton = Button.TTTButton("Menu", RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0.8, DISPLAY_HEIGHT * 0.8, DISPLAY_WIDTH * 0.4 / 2, DISPLAY_HEIGHT * 0.1 * 2))
    party = Party()
    user_pokemon = Pokemon()
    party.add_to_party(user_pokemon)
    print(user_pokemon.party_slot)
    enemy_pokemon = Pokemon()
    whatthefuck = TypeEffectiveness()
    intro = True
    global move_chosen
    global wait_time

    while intro == True:
        screen.fill(DARK_GRAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in Buttonmovelist:
                    if hovered_by_mouse(button):
                        for move in user_pokemon.movelist:
                            if button.text == move.name:
                                user_pokemon.select_player_move(move)
                                enemy_pokemon.select_enemy_move()
                                move_chosen = True
                                Buttonmovelist = []
                                wait_time = pygame.time.get_ticks()
                
                # menu button
                if hovered_by_mouse(MenuButton) and Battlemenulist != []:
                    Battlemenulist = []
                elif hovered_by_mouse(MenuButton):
                    Battlemenulist.append(Button.TTTButton("Run", RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0.8, DISPLAY_HEIGHT * 0.7, length / 2, height)))
                    Battlemenulist.append(Button.TTTButton("Bag", RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0.8, DISPLAY_HEIGHT * 0.6, length / 2, height)))
                    Battlemenulist.append(Button.TTTButton("Pokemon", RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0.8, DISPLAY_HEIGHT * 0.5, length / 2, height)))

                # menu list
                for button in Battlemenulist:
                    if hovered_by_mouse(button):
                        if button.text == "Run":
                            game_intro()
                        elif button.text == "Pokemon":
                            counter = 0
                            for y in range(3): # rows
                                for x in range(2): # cols
                                    pokemon = party.party_list[counter]
                                    if pokemon != None:
                                        Pokemonlist.append(Button.TTTButton(f'{pokemon.name} HP:{pokemon.HPcurrent}', RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0 + (x * length), DISPLAY_HEIGHT * 0.5 + (y * height), length, height)))
                                    elif pokemon == None:
                                        Pokemonlist.append(Button.TTTButton(f'Empty', RED, BRIGHT_RED, medText, pygame.Rect(DISPLAY_WIDTH * 0 + (x * length), DISPLAY_HEIGHT * 0.5 + (y * height), length, height)))
                                    #print(x_start + (x * x_change), y_start + (y * y_change), length, height)
                                    counter += 1
                            

                for button in Battlemenulist:
                    if button.text == "Pokemon":
                        if not hovered_by_mouse(button):
                            Pokemonlist = []
                            

                if not hovered_by_mouse(MenuButton):
                    Battlemenulist = []
                


        def check_for_pokemon_death():
            global move_chosen # game breaks when pokemon dies because move_chosen is still true

            if user_pokemon.HPcurrent <= 0:
                create_text(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2, medText, 'You Fainted', WHITE, BLACK, True)
                
                pygame.display.update()
                pygame.time.wait(2000)
                move_chosen = False
                game_intro()
                
            elif enemy_pokemon.HPcurrent <= 0:
                create_text(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2, medText, 'You Won!', WHITE, BLACK, True)
                
                pygame.display.update()
                pygame.time.wait(2000)
                move_chosen = False
                game_intro()

        def battle(user_pokemon, enemy_pokemon):
            global wait_time
            global went
            global move_chosen

            #who is faster?
            #user wins tie breakers for rn
            if user_pokemon.SPD >= enemy_pokemon.SPD:
                faster = user_pokemon
                slower = enemy_pokemon
            elif enemy_pokemon.SPD > user_pokemon.SPD:
                faster = enemy_pokemon
                slower = user_pokemon

            if pygame.time.get_ticks() - wait_time <= 4000:

                if went == False:
                    faster.attack(slower)
                    went = True
                create_text((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2) + 50, smallText, f'{faster.name} used {faster.selected_move.name} and did {faster.damage} damage.{faster.howeffectivewasit}', WHITE, BLACK, True)
            if pygame.time.get_ticks() - wait_time >= 4000 and pygame.time.get_ticks() - wait_time <= 5000:
                went = False
                check_for_pokemon_death()
            if pygame.time.get_ticks() - wait_time >= 5000 and pygame.time.get_ticks() - wait_time <= 9000:

                if went == False:
                    slower.attack(faster)
                    went = True
                create_text((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2) + 100, smallText, f'{slower.name} used {slower.selected_move.name} and did {slower.damage} damage.{slower.howeffectivewasit}', WHITE, BLACK, True)
            if pygame.time.get_ticks() - wait_time >= 9000:
                went = False
                move_chosen = False
                check_for_pokemon_death()

        if move_chosen == True:
            battle(user_pokemon, enemy_pokemon)

        def display_pokemoves():
            Buttonmovelist.append(Button.TTTButton(f'{user_pokemon.move1.name}', pokecolors[user_pokemon.move1.type], LIGHT_GRAY, medText, pygame.Rect(DISPLAY_WIDTH * 0.0, DISPLAY_HEIGHT * .8, length, height)))
            Buttonmovelist.append(Button.TTTButton(f'{user_pokemon.move2.name}', pokecolors[user_pokemon.move2.type], LIGHT_GRAY, medText, pygame.Rect(length, DISPLAY_HEIGHT * .8, length, height)))
            Buttonmovelist.append(Button.TTTButton(f'{user_pokemon.move3.name}', pokecolors[user_pokemon.move3.type], LIGHT_GRAY, medText, pygame.Rect(DISPLAY_WIDTH * 0.0, DISPLAY_HEIGHT * .9, length, height)))
            Buttonmovelist.append(Button.TTTButton(f'{user_pokemon.move4.name}', pokecolors[user_pokemon.move4.type], LIGHT_GRAY, medText, pygame.Rect(length, DISPLAY_HEIGHT * .9, length, height)))
            # "runs" the buttons
            # battle menu button ################################################################
            mouse = pygame.mouse.get_pos()
            MenuButton.brighten(mouse)
            pygame.draw.rect(screen, MenuButton.current_color, MenuButton.rect)
            pygame.draw.rect(screen, BLACK, MenuButton.rect, 1)
            blit_text(MenuButton)
            #####################################################################################
            # poke move buttons
            for button in Buttonmovelist:
                button.brighten(mouse)
                pygame.draw.rect(screen, button.current_color, button.rect)
                pygame.draw.rect(screen, BLACK, button.rect, 1)
                blit_text(button)
                # displays preview of how effective the move will be before selecting it
                if hovered_by_mouse(button):
                    zzz = list(pokecolors.keys())[list(pokecolors.values()).index(button.base_color)]
                    effectiveness = whatthefuck.calculate_effectiveness(zzz, enemy_pokemon.type1, enemy_pokemon.type2)
                    if effectiveness == 0:
                        howeffectivewasit = "immune"
                    elif effectiveness > 1:
                        howeffectivewasit = "super effective"
                    elif effectiveness == 1:
                        howeffectivewasit = "neutral"
                    elif effectiveness < 1:
                        howeffectivewasit = "not really effective"
                    create_text(button.rect.centerx, button.rect.centery + 20, smallText, howeffectivewasit, WHITE, None, True)

        def display_HP_bars(who, HPbarcolor, outlinecolor, outlinethickness, x, y, length, height):
            # changing hp bar colors at certain thresholds
            if who.HPtransition <= 0.1:
                HPbarcolor = RED
            elif who.HPtransition <= 0.5:
                HPbarcolor = YELLOW
            #slowly change hp bar when damaged
            if who.HPtransition > (who.HPcurrent / who.HPmax):
                who.HPtransition -= .01
            #create a button that changes size
            bu = Button.Button(HPbarcolor, HPbarcolor, pygame.Rect(x, y, who.HPtransition * length, height))
            pygame.draw.rect(screen, bu.current_color, bu.rect)
            #create an outline
            pygame.draw.rect(screen, outlinecolor, (x, y, length, height), outlinethickness)

        def display_everything():
            global move_chosen

            #user
            create_text(0, 0, medText, f'Level {user_pokemon.Level} {user_pokemon.name}', WHITE, BLACK)
            create_text(0, 30, medText, f'{user_pokemon.type1}', WHITE, pokecolors[user_pokemon.type1])
            if user_pokemon.type2:
                create_text((DISPLAY_WIDTH * 0.2), 30, medText, f'{user_pokemon.type2}', WHITE, pokecolors[user_pokemon.type2])
            create_text(0, 60, medText, f'HP: {user_pokemon.HPcurrent}', WHITE, RED)
            display_HP_bars(user_pokemon, GREEN, YELLOW, 1, 50, 100, 150, 30)
            #enemy
            create_text((DISPLAY_WIDTH/2), 0, medText, f'Level {enemy_pokemon.Level} {enemy_pokemon.name}', WHITE, BLACK)
            create_text((DISPLAY_WIDTH/2), 30, medText, f'{enemy_pokemon.type1}', WHITE, pokecolors[enemy_pokemon.type1])
            if enemy_pokemon.type2:
                create_text((DISPLAY_WIDTH/2) + (DISPLAY_WIDTH * 0.2),30, medText, f'{enemy_pokemon.type2}', WHITE, pokecolors[enemy_pokemon.type2])
            create_text((DISPLAY_WIDTH/2), 60, medText, f'HP: {enemy_pokemon.HPcurrent}', WHITE, RED)
            display_HP_bars(enemy_pokemon, GREEN, YELLOW, 1, (DISPLAY_WIDTH/2) + 50, 100, 150, 30)

            if move_chosen == False:
                display_pokemoves()
                for button in Battlemenulist:
                    mouse = pygame.mouse.get_pos()
                    button.brighten(mouse)
                    pygame.draw.rect(screen, button.current_color, button.rect)
                    pygame.draw.rect(screen, BLACK, button.rect, 1)
                    blit_text(button)
                for button in Pokemonlist:
                    mouse = pygame.mouse.get_pos()
                    button.brighten(mouse)
                    pygame.draw.rect(screen, button.current_color, button.rect)
                    pygame.draw.rect(screen, BLACK, button.rect, 1)
                    blit_text(button)

            
            #display fps
            create_text(DISPLAY_WIDTH*0.95, 0, smallText, f'{round(clock.get_fps())}', WHITE, BLACK)

            clock.tick(30)
            pygame.display.update()

        display_everything()


game_intro()

# sprites at some point
