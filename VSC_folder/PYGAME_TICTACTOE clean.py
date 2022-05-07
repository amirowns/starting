
import pygame
import sys
import Button 

# colors for text
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (24, 25, 26)
LIGHT_GRAY = (58, 59, 60)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (40, 255, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 40, 0)

# create a clock to track time
clock = pygame.time.Clock()

# set up pygame and its screen
pygame.init()
display_width = 600
display_height = 600
screen_size = (display_width, display_height)
screen = pygame.display.set_mode(screen_size)

# add window caption
pygame.display.set_caption('Tic Tac Toe')

# set up font and text; size=25, bold=True, italic=False
smallText = pygame.font.SysFont("Arial", 25, True, False)
largeText = pygame.font.SysFont('Arial', 100, True, False)

def draw_tic_tac_toe():
    # draws the tictactoe grid
    pygame.draw.line(screen, WHITE, [display_width * 1/3 , display_height * 0], [display_width * 1/3, display_height * 1], 2) #left vertical line
    pygame.draw.line(screen, WHITE, [display_width * 2/3 , display_height * 0], [display_width * 2/3, display_height * 1], 2) #right vertical line
    pygame.draw.line(screen, WHITE, [display_width * 0 , display_height * 1/3], [display_width * 1, display_height * 1/3], 2) #upper horizontal line
    pygame.draw.line(screen, WHITE, [display_width * 0 , display_height * 2/3], [display_width * 1, display_height * 2/3], 2) #lower horizontal line

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

# puts large text in middle of screen
def message_display(text):
    largeText = pygame.font.SysFont('Arial', 100, True, False)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
        
# the start menu 
def game_intro():

    intro = True

    MM_Button_list = []
    screen.fill(BLACK)
    message_display("Tic Tac Toe")


    # make buttons
    green_button = Button.TTTButton("Start", GREEN, BRIGHT_GREEN, smallText, pygame.Rect(display_width * 0.2, display_height * .75, display_width * 0.2, display_height * 0.1))
    red_button = Button.TTTButton("Quit", RED, BRIGHT_RED, smallText, pygame.Rect(display_width * 0.6, display_height * .75, display_width * 0.2, display_height * 0.1))
    
    # add buttons to button list
    MM_Button_list.append(green_button)
    MM_Button_list.append(red_button)

    while intro:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in MM_Button_list:
                    if button.hovered(mouse):
                        # enlarges button when hovered
                        button.rect = pygame.Rect.inflate(button.rect, 20, 20)
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in MM_Button_list:
                    if button.hovered(mouse):
                        if button.text == "Start":
                            game_loop()
                            break
                        elif button.text == "Quit":
                            sys.exit()
    

                    
            else: 
                pass

        # "runs" the buttons
        for button in MM_Button_list:
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)
            textSurf, textRect = button.text_objects
            textRect.center = (button.rect.center)
            screen.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)

# the main tic tac toe game
def game_loop():

    game = True
    Turncount = 0

    # fills screen with a background color
    screen.fill(BLACK)
    TTT_Button_list = []
    
    # makes the buttons easily
    Top_Left = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 0, display_height * 0, display_width * 1/3, display_height * 1/3))
    Top_Middle = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 1/3, display_height * 0, display_width * 1/3, display_height * 1/3))
    Top_Right = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 2/3, display_height * 0, display_width * 1/3, display_height * 1/3))
    Middle_Left = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 0, display_height * 1/3, display_width * 1/3, display_height * 1/3))
    Middle_Middle = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 1/3, display_height * 1/3, display_width * 1/3, display_height * 1/3))
    Middle_Right = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 2/3, display_height * 1/3, display_width * 1/3, display_height * 1/3))
    Bottom_Left = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 0, display_height * 2/3, display_width * 1/3, display_height * 1/3))
    Bottom_Middle = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 1/3, display_height * 2/3, display_width * 1/3, display_height * 1/3))
    Bottom_Right = Button.TTTButton(None, DARK_GRAY, LIGHT_GRAY, largeText, pygame.Rect(display_width * 2/3, display_height * 2/3, display_width * 1/3, display_height * 1/3))

    # add buttons to list
    TTT_Button_list.append(Top_Left)
    TTT_Button_list.append(Top_Middle)
    TTT_Button_list.append(Top_Right)
    TTT_Button_list.append(Middle_Left)
    TTT_Button_list.append(Middle_Middle)
    TTT_Button_list.append(Middle_Right)
    TTT_Button_list.append(Bottom_Left)
    TTT_Button_list.append(Bottom_Middle)
    TTT_Button_list.append(Bottom_Right)

    while game:

        # gets the mouse position
        mouse = pygame.mouse.get_pos()

        # handle mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # somehow like a pause button cause the "X"s dont dissapear
                    game_intro()
                    break
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('mouse button is pressed')
                mouse_pos = event.pos
                print(mouse_pos)
                for button in TTT_Button_list:
                    if button.hovered(mouse):
                        if Turncount % 2 == 0:
                            # puts an X in the clicked TTT button, cant overwrite another "X" or "O"
                            if button.text != "X" and button.text != "O":
                                Turncount += 1
                                button.Add_text_to_button("X")
                        elif Turncount % 2 != 0:
                            # puts an O in the clicked TTT button
                            if button.text != "X" and button.text != "O":
                                Turncount += 1
                                button.Add_text_to_button("O")

        # "runs" the button
        for button in TTT_Button_list:
            button.brighten(mouse)
            pygame.draw.rect(screen, button.current_color, button.rect)
            textSurf, textRect = button.text_objects
            textRect.center = (button.rect.center)
            screen.blit(textSurf, textRect)
                            
        draw_tic_tac_toe()

        # logic for winning
        # checks for win
        if (Top_Left.text == "X" and Top_Middle.text == "X" and Top_Right.text == "X") or \
            (Middle_Left.text == "X" and Middle_Middle.text == "X" and Middle_Right.text == "X") or \
            (Bottom_Left.text == "X" and Bottom_Middle.text == "X" and Bottom_Right.text == "X") or \
            (Top_Left.text == "X" and Middle_Left.text == "X" and Bottom_Left.text == "X") or \
            (Top_Middle.text == "X" and Middle_Middle.text == "X" and Bottom_Middle.text == "X") or \
            (Top_Right.text == "X" and Middle_Right.text == "X" and Bottom_Right.text == "X") or \
            (Top_Left.text == "X" and Middle_Middle.text == "X" and Bottom_Right.text == "X") or \
            (Top_Right.text == "X" and Middle_Middle.text == "X" and Bottom_Left.text == "X"):
                screen.fill(BLACK)
                message_display("X WINS!")
                break
                
        elif (Top_Left.text == "O" and Top_Middle.text == "O" and Top_Right.text == "O") or \
            (Middle_Left.text == "O" and Middle_Middle.text == "O" and Middle_Right.text == "O") or \
            (Bottom_Left.text == "O" and Bottom_Middle.text == "O" and Bottom_Right.text == "O") or \
            (Top_Left.text == "O" and Middle_Left.text == "O" and Bottom_Left.text == "O") or \
            (Top_Middle.text == "O" and Middle_Middle.text == "O" and Bottom_Middle.text == "O") or \
            (Top_Right.text == "O" and Middle_Right.text == "O" and Bottom_Right.text == "O") or \
            (Top_Left.text == "O" and Middle_Middle.text == "O" and Bottom_Right.text == "O") or \
            (Top_Right.text == "O" and Middle_Middle.text == "O" and Bottom_Left.text == "O"):
                screen.fill(BLACK)
                message_display("O WINS!")
                break
                
        elif Turncount == 9:
            screen.fill(BLACK)
            message_display("IT'S A TIE!")
            break

        pygame.display.update()

        # limit the update to 60 frames per second
        clock.tick(60)

game_intro()

