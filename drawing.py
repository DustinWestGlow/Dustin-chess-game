import pygame
from variables import *
import engine

def color_tile(row, col, color):
    tile = pygame.Rect(tile_size * col, tile_size * (7 - row), tile_size, tile_size)
    pygame.draw.rect(screen, color, tile)

def draw_piece(piece):
    # https://stackoverflow.com/questions/8873219/how-can-i-draw-images-and-sprites-in-pygame
    img_key = piece.color + '_' + piece.piece
    image_surface = images[img_key]
    # the data is represented correctly in the arrays
    # but I'm a noob at flipping the canvas
    row = (7 - piece.position[0]) # 8 - row because of canvas being top-down
    col = piece.position[1]
    x = ((tile_size - piece_size)// 2) + (col * piece_size) + ((tile_size - piece_size) * col)
    y = ((tile_size - piece_size)// 2) + (row * piece_size) + ((tile_size - piece_size) * row)
    screen.blit(image_surface, (x, y))

def draw_board():
    # first draw tiles
    flop_colors = [colors['white'], colors['black']]
    turn_color = (255, 255, 150)
    flopper = 0
    for row in range(8):
        for col in range(8):
            flopper = (flopper + 1) % 2 # put left-bottom tile (0, 0) black
            which_color = flop_colors[flopper]
            color_tile(row, col, which_color)
        flopper = (flopper + 1) % 2
    # highlight which player's move with tile
    turn = engine.get_turn()
    if turn.color == 'white':
        color_tile(0, 7, turn_color)
    else:
        color_tile(7, 0, turn_color)
    # highlight desired tiles
    picked = engine.get_picked()
    if picked:
        color_tile(picked.position[0], picked.position[1], colors['desire'])
    # then draw pieces
    players = engine.get_players()
    for player in players:
        for piece in player.pieces:
            draw_piece(piece)
