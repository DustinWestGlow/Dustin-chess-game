from variables import *
import pygame
from drawing import *

FOO = Player('foo', 'white')
BAR = Player('bar', 'black')
PICKED = None
PLAYERS = [FOO, BAR]
TI = 0
TURN = PLAYERS[TI]
OTHER = PLAYERS[(TI + 1) % 2]

def get_picked():
    return PICKED
def get_players():
    return PLAYERS
def get_turn():
    return TURN

replay_index = 0
replay_sequence = []
with open('records/temp.txt', 'r') as file:
    replay_sequence
    replay_sequence.append("BEGINNING")
    for line in file:
        line = line.rstrip()
        non_numbered = line.split('/')[1]
        move_pair = non_numbered.split('.')
        print(move_pair)
        white = move_pair[0]
        replay_sequence.append(white)
        if move_pair[1] == '':
            break
        black = move_pair[1]
        replay_sequence.append(black)
    replay_sequence.append('END')
print(replay_sequence)

def make_move(code):
    print(code)

def replay_next():
    global replay_index
    if replay_index == (len(replay_sequence) - 1):
        return
    replay_index += 1
    m = replay_sequence[replay_index]
    if m == "END":
        return
    make_move(m)

def replay_prev():
    global replay_index
    if replay_index == 0:
        return
    replay_index -= 1
    m = replay_sequence[replay_index]
    if m == "BEGINNING":
        return
    make_move(m)
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
def to_grid(pos):
    col = pos[0] // tile_size
    row = 7 - (pos[1] // tile_size)
    return (row, col)

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

def handle_click(pos):
    color_tile(pos[0], pos[1], colors['desire'])

mousedown_flag = False # initialize value
keydown_flag = False
def handle_events(mode):
    global mousedown_flag
    getters = pygame.event.get()
    mousedown = pygame.mouse.get_pressed()[0]
    if mousedown and not mousedown_flag:
        mousedown_flag = True
        handle_click(pygame.mouse.get_pos())
    if not mousedown:
        mousedown_flag = False
    global keydown_flag
    if mode == 'replay':
        for event in getters:
            if event.type == pygame.QUIT:
                # sys.exit()
                pass
            if event.type == pygame.KEYDOWN:
                left = event.key == pygame.K_LEFT
                right = event.key == pygame.K_RIGHT
                keydown = True in {left, right}
                if keydown and not keydown_flag:
                    keydown_flag == True
                    if left:
                        replay_prev()
                    elif right:
                        replay_next()
                if not keydown:
                    keydown_flag = False

def handle_click(pos):
    global PICKED
    global TURN
    global OTHER
    global TI
    clicked_tile = to_grid(pos)
    in_your_pieces = is_yours(clicked_tile)
    picked_piece = get_piece(clicked_tile)
    if not in_your_pieces:
        if valid_move(PICKED, clicked_tile):
            # if killed piece, animate and affect data
            if picked_piece and (clicked_tile == picked_piece.position):
                OTHER.die(picked_piece)
            TI = (TI + 1) % 2
            TURN = PLAYERS[TI]
            OTHER = PLAYERS[(TI + 1) % 2]
            PICKED.move(clicked_tile)
        PICKED = None
    else:
        PICKED = picked_piece

mouse_flag = False
def update():
    pass