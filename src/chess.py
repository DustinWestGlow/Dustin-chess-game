import random
import time
import sys

import pygame
from pygame.locals import *
pygame.init()

from variables import *
from definitions import *
from get_assets import *
from drawing import *
from engine import *
from events import *

main_game = ChessGame()
# main_game.board.print_board()

FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Chess")

DEBUG = False
mode = 'play'
if 'replay' in sys.argv:
    mode = 'replay'
def main():
    main_game = ChessGame()
    board = main_game.board
    generate_piece_images(images, piece_edge_pixel_count)
    while True:
        getters = pygame.event.get()
        handle_mouse(getters, board, mode)
        handle_keyboard(getters, board, mode)
        handle_possible_close(getters)
        draw_board(board)
        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == '__main__':
    main()