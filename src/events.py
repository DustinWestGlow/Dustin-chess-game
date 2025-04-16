import sys
from variables import *
import engine

# initialize flags
mousedown_flag = False
def handle_mouse(getters, board, mode):
    global mousedown_flag
    mousedown = pygame.mouse.get_pressed()[0]
    if mousedown and not mousedown_flag:
        mousedown_flag = True
        # TODO: allow for GUI mousing further into dev
        clicked_tile = coordinate_to_position(board, pygame.mouse.get_pos())
        engine.tile_action(board, clicked_tile)
    if not mousedown:
        mousedown_flag = False
    
keydown_flag = False
def handle_keyboard(getters, board, mode):
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

def coordinate_to_position(board, coordinate):
    mouse_x = coordinate[0]
    mouse_y = coordinate[1]
    # TODO: Update 0's to 'board_coords.x/.y'
    # For future non-top-left located board, return outofrange
    if mouse_x < 0 or mouse_y < 0:
        return None
    # if there's a GUI or other thing beyond the board
    # don't return a valid tile, return an outofrange
    # again, TODO: use board_coords
    if mouse_x >= BOARD_WIDTH or mouse_y >= BOARD_HEIGHT:
        return None
    row = zero_indexed_tile_count - (mouse_y // tile_edge_pixel_count)
    col = mouse_x // tile_edge_pixel_count
    return (row, col)

def handle_possible_close(getters):
    if pygame.QUIT in [event.type for event in getters]:
        pygame.quit()
        sys.exit()