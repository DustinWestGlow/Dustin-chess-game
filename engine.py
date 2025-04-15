from variables import *
import pygame
from drawing import *
import sys

import replay

def frontier(player):
    return
def valid_move(piece, tile):
    if piece == None:
        return False
    return True
    # return [(0, 0)]

# Input is a tuple: (x, y) in pixels the cursor coordinates
# Output a tuple: (row, col) of the tile containing cursor
# Cursor position -> corresponding Tile
# def to_grid(pos):
#     col = pos[0] // tile_size
#     row = 7 - (pos[1] // tile_size)
#     return (row, col)

# Input is a Tile tuple: (row, col)
# Output is a Piece instance or None
# If the input tile has a chess piece on it, return that piece
# (specifically a chess piece of the current player)
# otherwise, return None 
# which Tile -> Piece instance or None
def is_yours(tile):
    for piece in TURN.pieces:
        if piece.position == tile:
            return True
    return False

def get_piece(tile):
    for player in PLAYERS:
        for piece in player.pieces:
            if piece.position == tile:
                return piece
    return None


# initialize flags
mousedown_flag = False
def handle_mouse(getters, mode):
    global mousedown_flag
    mousedown = pygame.mouse.get_pressed()[0]
    if mousedown and not mousedown_flag:
        mousedown_flag = True
        # handle_click(pygame.mouse.get_pos())
    if not mousedown:
        mousedown_flag = False

def handle_possible_close(getters):
    if pygame.QUIT in [event.type for event in getters]:
        pygame.quit()
        sys.exit()

keydown_flag = False
def handle_keyboard(getters, mode):
    global keydown_flag
    if mode == 'play':
        return
    keydown = pygame.KEYDOWN in [event.type for event in getters]
    if keydown and not keydown_flag:
        keydown_flag = True
        for event in getters:
            if event.key == pygame.K_LEFT:
                print("left")
                # replay.replay_prev()
            elif event.key == pygame.K_RIGHT:
                print("right")
                    # replay.replay_next()
    if not keydown:
        keydown_flag = False
    
    


# def handle_click(pos):
#     # TODO:
#     # - allow clicking to select and move pieces in data
#     # - allow selected pieces in data to generate possible moves
#     #   - and show those moves
#     color_tile(pos[0], pos[1], colors['desire'])

# TODO: "fix"
# def handle_choice(clicked_tile):
#     if valid_move(PICKED, clicked_tile):
#         # if killed piece, animate and affect data
#         if picked_piece and (clicked_tile == picked_piece.position):
#             OTHER.die(picked_piece)
#         TI = (TI + 1) % 2
#         TURN = PLAYERS[TI]
#         OTHER = PLAYERS[(TI + 1) % 2]
#         PICKED.move(clicked_tile)

# TODO
# - use 'coordinates' for mouse and drawing pixels
# - use 'position' for board positions
# - redo variable names, stop the global vars, use class state
# def handle_click(pos):
#     global PICKED
#     global TURN
#     global OTHER
#     global TI
#     # Position
#     clicked_tile = to_grid(pos)
#     # Boolean
#     in_your_pieces = is_yours(clicked_tile)
#     # Piece
#     picked_piece = get_piece(clicked_tile)
#     # Create a flowchart or similar to make this conditional easy to grasp
#     if not in_your_pieces:
#         if PICKED:
#             handle_choice(clicked_tile)
#         else:
#             PICKED = None
#     else:
#         PICKED = picked_piece

def update():
    pass