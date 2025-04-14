import pygame
from structures import *

# 8 tiles x 8 tiles
# each tile is 64x64 pixels
tile_size = 64
piece_size = 54
HEIGHT = tile_size * 8
WIDTH = tile_size * 8
FPS = 30
FFF = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_hash = {
    'foo': 'white',
    'bar': 'black'
}

images = dict()

colors = {
    'desire': (15, 100, 255),
    'white': (230, 232, 195),
    'black': (92, 140, 70),
}

piece_position_list = []


