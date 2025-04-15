# Input is a tuple: (x, y) in pixels the cursor coordinates
# Output a tuple: (row, col) of the tile position containing cursor
# Cursor coordinates -> corresponding Tile position
board_edge_tiles = 8
tile_edge_pixels = 64
board = {
    'width': tile_edge_pixels * board_edge_tiles,
    'height': tile_edge_pixels * board_edge_tiles
}
def coordinate_to_position(coordinate):
    mouse_x = coordinate[0]
    mouse_y = coordinate[1]
    # TODO: Update 0's to 'board_coords.x/.y'
    # For future non-top-left located board, return outofrange
    if mouse_x < 0 or mouse_y < 0:
        return None
    # if there's a GUI or other thing beyond the board
    # don't return a valid tile, return an outofrange
    # again, TODO: use board_coords
    if mouse_x >= board['width'] or mouse_y >= board['height']:
        return None
    col = mouse_x // tile_edge_pixels
    row = board_edge_tiles - (mouse_y // tile_edge_pixels)
    # because positions are zero-indexed,
    # but board tile count is one-indexed
    row = row - 1 
    return (row, col)