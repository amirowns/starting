import json
from functools import reduce
from pygame import display
import time
import ast
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "teppelin.net"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        try:
            self.client.send(data)
            reply = self.client.recv(2048).decode()
            return reply

        except socket.error as e:
            return str(e)


def HandleInput(player):
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.moveRight()
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.moveLeft()
    
    if pygame.key.get_pressed()[pygame.K_UP]:
        player.moveUp()
    
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player.moveDown()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

class Data:
    def __init__(self, players):
        self.players = players
        self.playerRects = {}

        for player in self.players:
            self.playerRects[player.playerId] = player.rect

    def UpdatePlayerLocation(self, playerId, rect):
        self.playerRects[playerId] = rect
    
    def GetEncodedRect(self):
        
        data = {playerId : self.playerRects[playerId]}
        print(data)
        return str.encode(str(data))

    def DecodeRects(self, playerRect):
        print(playerRect.decode('utf-8'))

class Player:
    def __init__(self, screen, color, rect, playerId):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.horizontalSpeed = 10
        self.verticalSpeed = 10
        self.playerId = playerId
        self.serverRect  = None

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, self.color, self.rect)
        self.serverRect  = (self.rect.left, self.rect.top, self.rect.width, self.rect.height)

    def moveRight(self):
        if self.rect.right < display_width:
            self.rect = self.rect.move(self.horizontalSpeed, 0)
    
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect = self.rect.move(-self.horizontalSpeed, 0)
    
    def moveUp(self):
        if self.rect.top > 0:
            self.rect = self.rect.move(0, -self.verticalSpeed)
    
    def moveDown(self):
        if self.rect.bottom < display_height:
            self.rect = self.rect.move(0, self.verticalSpeed)

import pygame
import sys

from pygame.constants import K_DOWN, K_UP

network = Network()
playerId = int(network.connect())
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
playerStates = {}

players = []
players.append(Player(screen, GREEN, (display_width * 0.2, display_height * .75, display_width * 0.2, display_height * 0.1), 0))
players.append(Player(screen, RED, (display_width * 0.2, display_height * .75, display_width * 0.2, display_height * 0.1), 1))
myPlayer = players[playerId]

gameData = Data(players)

while True:
    screen.fill(BLACK)
    #players = gameData.players

    HandleInput(myPlayer)
    gameData.UpdatePlayerLocation(myPlayer.playerId, myPlayer.serverRect)
    
    reply = network.send(gameData.GetEncodedRect())
    replyJson = ast.literal_eval(reply)
    playerStates.update(replyJson)

    if 0 in playerStates and 1 in playerStates:
    
        if playerStates[0] != None and playerStates[1] != None:
            if playerId == 0:
                players[1].rect.left = playerStates[1][0]
                players[1].rect.top = playerStates[1][1]
                players[1].rect.width = playerStates[1][2]
                players[1].rect.height = playerStates[1][3]

            if playerId == 1:
                players[0].rect.left = playerStates[0][0]
                players[0].rect.top = playerStates[0][1]
                players[0].rect.width = playerStates[0][2]
                players[0].rect.height = playerStates[0][3]

    print(reply)
    #gameData.DecodeRects(gameData.GetEncodedRects())
    
    for player in players:
        player.draw()

    pygame.display.update()

    # limit the update to 60 frames per second
    clock.tick(60)
