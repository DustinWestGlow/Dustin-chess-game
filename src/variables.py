import pygame
from definitions import *

# 8 tiles x 8 tiles
# each tile is 64x64 pixels
board_edge_tile_count = 8
zero_indexed_tile_count = board_edge_tile_count - 1
tile_edge_pixel_count = 64
piece_edge_pixel_count = 54
side_length = board_edge_tile_count * tile_edge_pixel_count
BOARD_WIDTH = side_length
BOARD_HEIGHT = side_length
GUI_WIDTH = 0
GUI_HEIGHT = 0
SCREEN_WIDTH = GUI_WIDTH + BOARD_WIDTH
SCREEN_HEIGHT = GUI_HEIGHT + BOARD_HEIGHT
FPS = 30
FFF = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_hash = {
    'foo': 'white',
    'bar': 'black'
}

images = dict()

colors = {
    'selected': (15, 100, 255),
    'white': (230, 232, 195),
    'black': (92, 140, 70),
    'turn': (255, 255, 150)
}

piece_position_list = []


role_hash = {
    'pawn': ['pawn' for column in range(board_edge_tile_count)],
    'specialist': ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
}
row_indexes = {
    'pawn': {
        'white': 1,
        'black': 6
    },
    'specialist': {
        'white': 0,
        'black': 7
    }
}
turn_flipper = {
    'white': 'black',
    'black': 'white'
}