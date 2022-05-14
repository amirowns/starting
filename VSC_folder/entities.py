import json
import pygame

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 800


class Entity():
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def toJSON(self):
    
        jsonDATA = {}
        entityStats = {}
        entityStatsList = []

        entityStats["health"] = self.health
        entityStats["attack"] = self.attack
        entityStats["defense"] = self.defense

        jsonDATA["entity"] = entityStats

        return json.dumps(jsonDATA)
    


class Player(Entity):
    def __init__(self):
        self.name = "player"
        self.health = 10
        self.max_health = self.health
        self.current_health = self.health
        self.attack = 1
        self.defense = 0
        self.image = pygame.image.load("VSC_folder/pictures/Player.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center =  DISPLAY_WIDTH * 0.3, DISPLAY_HEIGHT * 0.3


class Goblin(Entity):
    def __init__(self):
        self.health = 5
        self.max_health = self.health
        self.current_health = self.health
        self.attack = 1
        self.defense = 0 
        self.image = pygame.image.load("VSC_folder/pictures/goblin.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH * 0.6, DISPLAY_HEIGHT * 0.3
    