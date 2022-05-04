WHITE = (255, 255, 255)

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

class Button(object):
    def __init__(self, text, base_color, bright_color, font, rect):
    
        self.text = text
        self.base_color = base_color
        self.bright_color = bright_color
        self.font = font
        self.rect = rect
        self.current_color = self.base_color
        self.text_objects = text_objects(text, font)

    # checks if the button is being hovered
    def hovered(self, mouse):
        return self.rect.collidepoint(mouse)

    # changes the button to be brighter upon hover
    def brighten(self, mouse):
        if self.hovered(mouse):
            self.current_color = self.bright_color
        else:
            self.current_color = self.base_color

###################################################################### for TTT buttons
    # puts text in the button
    def Add_text_to_button(self, text):
        self.text = text
        self.text_objects = text_objects(text, self.font)
    
    # puts an opaque X while hovering button
    def PreviewText(self, text, mouse):
        if self.hovered(mouse):
            self.text = text
            self.text_objects = text_objects(text, self.font)
        else: 
            pass