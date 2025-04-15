import pygame
from variables import *
import engine

def color_tile(position, color):
    row = position[0]
    col = position[1]
    # validate inputs
    if row < 0 or col < 0:
        raise ValueError
    max_val = board_edge_tile_count
    if row > max_val or col > max_val:
        raise ValueError
    tile_edge = tile_edge_pixel_count
    tile_x = tile_edge * col
    tile_y = tile_edge * (zero_indexed_tile_count - row)
    tile = pygame.Rect(tile_x, tile_y, tile_edge, tile_edge)
    pygame.draw.rect(screen, color, tile)

def draw_piece(piece):
    if not piece:
        return
    # https://stackoverflow.com/questions/8873219/how-can-i-draw-images-and-sprites-in-pygame
    img_key = piece.color + '_' + piece.role
    image_surface = images[img_key]
    row = (zero_indexed_tile_count - piece.position[0])
    col = piece.position[1]
    tile_corner_to_piece_corner = (tile_edge_pixel_count - piece_edge_pixel_count) // 2
    cx = (col * tile_edge_pixel_count) + tile_corner_to_piece_corner
    cy = (row * tile_edge_pixel_count) + tile_corner_to_piece_corner
    coordinates = (cx, cy)
    # x = ((tile_size - piece_size)// 2) + (col * piece_size) + ((tile_size - piece_size) * col)
    # y = ((tile_size - piece_size)// 2) + (row * piece_size) + ((tile_size - piece_size) * row)
    screen.blit(image_surface, coordinates)

def draw_board(board):
    # first draw tiles
    flop_colors = [colors['white'], colors['black']]
    flopper = 0
    for row in range(8):
        for col in range(8):
            which_color = flop_colors[flopper]
            color_tile((row, col), which_color)
            flopper = (flopper + 1) % 2 # put left-bottom tile (0, 0) black
        flopper = (flopper + 1) % 2 # trick: even amount of columns
    # highlight which player's move with tile
    turn = board.state.turn
    if turn == 'white':
        color_tile((0, 7), colors['turn'])
    else:
        color_tile((7, 0), colors['turn'])
    # highlight desired tiles
    picked = board.state.picked
    if picked:
        color_tile(picked.position, colors['desire'])
    # then draw pieces
    for row in board.board:
        for piece in row:
            draw_piece(piece)