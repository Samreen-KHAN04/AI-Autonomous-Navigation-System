# ===============================
# helpers.py
# Utility functions & conversions
# ===============================

def grid_to_pixel(x, y, cell_size):
    """Convert grid coordinates (col,row) → pixel coordinates (px, py)."""
    return x * cell_size, y * cell_size


def pixel_to_grid(px, py, cell_size):
    """Convert pixel position → grid cell index."""
    return px // cell_size, py // cell_size


def is_within_bounds(x, y, width, height):
    """Check if a cell is inside the map."""
    return 0 <= x < width and 0 <= y < height