# example test
import pytest
from engine import coordinate_to_position

def test_coordinate_to_position():
    # Test some well-understood cases
    assert coordinate_to_position((0, 0)) == (7, 0)       # Top-left corner
    assert coordinate_to_position((64, 64)) == (6, 1)     # Assuming tile_size = 64
    assert coordinate_to_position((448, 448)) == (0, 7)   # Bottom-right corner
    
    # Test anything interesting you can think of, like stuff that should be in the same tile
    assert coordinate_to_position((0, 0)) == coordinate_to_position((63, 63))
    
    # Test some edge cases
    assert coordinate_to_position((0, 511)) == (0, 0)     # Bottom-left
    assert coordinate_to_position((511, 0)) == (7, 7)     # Top-right