import pygame
from variables import *
from drawing import *
from events import *

# import replay

def frontier(player):
    return

def valid_move(board, piece, position):
    if piece == None:
        return False
    return True
    # return [(0, 0)]

def tile_action(board, selected_tile):
    # when you select a tile OR piece
    newly_selected = board.get_piece_from_tile(selected_tile)
    # and you already have a piece previously selected
    # (a move requires the new select to be not one of your pieces)
    if board.state.previously_selected and not board.is_turn_piece(newly_selected):
        # you must be trying to move said piece
        ps = board.state.previously_selected
        # so test for valid movement
        if valid_move(board, ps, selected_tile):
            board.move(ps, selected_tile) # and knock it out!
    # if you selected one of your own pieces
    if board.is_turn_piece(newly_selected):
        # then just move the selection/highlighting to said piece
        board.state.previously_selected = newly_selected
    else:
        # otherwise, you're moving or capturing
        board.state.previously_selected = False

def update():
    pass