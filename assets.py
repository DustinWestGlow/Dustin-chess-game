import pygame

def generate_piece_images(images, piece_size):
    for color in ['white', 'black']:
        for piece in ['bishop', 'king', 'knight', 'pawn', 'queen', 'rook']:
            img_key = color + '_' + piece
            img_path = 'assets/' + color + '/' + piece + '.png'
            image = pygame.image.load(img_path).convert_alpha()
            image = pygame.transform.scale(image, (piece_size, piece_size))
            images[img_key] = image