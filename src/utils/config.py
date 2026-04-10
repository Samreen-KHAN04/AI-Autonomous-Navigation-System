# ===============================
# config.py
# Global configuration variables
# ===============================

GRID_WIDTH = 20          # number of columns
GRID_HEIGHT = 20         # number of rows
CELL_SIZE = 30           # pixel size per grid cell

WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Colors (R, G, B)
COLOR_BG = (30, 30, 30)
COLOR_GRID = (50, 50, 50)
COLOR_OBSTACLE = (200, 50, 50)
COLOR_PATH = (50, 200, 50)
COLOR_START = (50, 150, 255)
COLOR_GOAL = (255, 200, 0)
COLOR_ROBOT = (255, 255, 255)

ROBOT_SPEED = 0.2  # grid cells per frame