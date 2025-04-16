import pygame

import variables
# TODO: return an 8x8 board of Pieces and None
def init_board():
    nxn = variables.board_edge_tile_count
    result = [[None for column in range(nxn)] for row in range(nxn)]
    for color in ['white', 'black']:
        for role_hash_key in ['pawn', 'specialist']:
            for column in range(nxn):
                row = variables.row_indexes[role_hash_key][color]
                role = variables.role_hash[role_hash_key][column]
                result[row][column] = Chessman(color, role, (row, column))
    return result

class ChessGame():
    def __init__(self):
        self.board = Board()
        return
class Board():
    def __init__(self, coordinates=(0, 0)):
        self.board = init_board()
        self.state = GameState()
        self.players = [Player('white'), Player('black')]
        self.coordinates = coordinates
        return
    def print_board(self):
        for row in self.board:
            row_string = ''
            for piece in row:
                row_string += piece.__str__() + ' / '
            print(row_string)
    def get_piece_from_tile(self, tile):
        row = tile[0]
        col = tile[1]
        return self.board[row][col]
    def move(self, piece, new_position):
        old_row = piece.position[0]
        old_col = piece.position[1]
        new_row = new_position[0]
        new_col = new_position[1]
        self.board[old_row][old_col] = None
        self.board[new_row][new_col] = piece
        piece.position = new_position
        self.state.turn = variables.turn_flipper[self.state.turn]
    def is_turn_piece(self, piece):
        if not piece:
            return False
        return piece.color == self.state.turn

class GameState():
    def __init__(self):
        self.dead = []
        self.turn = 'white'
        self.previously_selected = None
        return
    def capture(self, moving_piece, dying_piece):
        return
        # self.dead.append([element for element in self.pieces if (p.position == element.position)][0])
        # self.pieces = [element for element in self.pieces if (not p.position == element.position)]

class Player():
    def __init__(self, name):
        self.name = name

# the official name for any single army soldier
class Chessman():
    def __init__(self, color, role, position):
        super().__init__()
        self.color = color
        self.role = role # the type of soldier
        self.position = position
    def move(self, position):
        self.position = position
    def console(self):
        print(self.color, self.piece, self.position)
    def __str__(self):
        return self.color + ', ' + self.role + ', ' + str(self.position)