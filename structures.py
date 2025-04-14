import pygame

class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces = []
        self.dead = []
        self.init_pieces()
    def die(self, p):
        self.dead.append([element for element in self.pieces if (p.position == element.position)][0])
        self.pieces = [element for element in self.pieces if (not p.position == element.position)]
    def init_pieces(self):
        pawn_row = -1
        special_row = -1
        if self.color == 'white':
            pawn_row = 1
            special_row = 0
        elif self.color == 'black':
            pawn_row = 6
            special_row = 7
        order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        pieces = []
        for col in range(8):
            pieces.append(
                Chessman(self.color, 'pawn', (pawn_row, col))
            )
        for col in range(8):
            pieces.append(
                Chessman(self.color, order[col], (special_row, col))
            )
        self.pieces = pieces

# the official name for any single army soldier
class Chessman():
    def __init__(self, color, piece, position):
        super().__init__()
        self.color = color
        self.piece = piece # the type of soldier
        self.position = position
    def move(self, position):
        self.position = position
    def console(self):
        print(self.color, self.piece, self.position)