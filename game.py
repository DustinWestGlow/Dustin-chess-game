import random
import time
import sys



from variables import *
from structures import *
from assets import *
from drawing import *
from engine import *

import pygame
from pygame.locals import *
pygame.init()

FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Chess")



DEBUG = False
mode = 'replay' # 'play'
keydown_flag = False
def main():
    generate_piece_images(images, piece_size)
    if DEBUG:
        pygame.quit()
        print("Debug Mode. Game Not Running.")
        # Put Debug code here, prints, etc.
        # print(PLAYERS[0].pieces)
        # for player in PLAYERS:
        #     for piece in player.pieces:
        #         print(piece)
        return # end Debug
    while True:
        handle_events(mode)
        update()
        draw_board()
        pygame.display.update()
        FramePerSec.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()