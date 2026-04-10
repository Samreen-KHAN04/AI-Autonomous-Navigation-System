import numpy as np
from random import randint
from src.utils.config import GRID_WIDTH, GRID_HEIGHT

class GridMap:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = np.zeros((self.width, self.height), dtype=int)

        self.start = (0, 0)
        self.goal = (self.width - 1, self.height - 1)

    def random_obstacles(self, count=60):
        """Place random obstacles in the grid."""
        for _ in range(count):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if (x, y) != self.start and (x, y) != self.goal:
                self.grid[x][y] = 1  # obstacle

    def is_obstacle(self, x, y):
        return self.grid[x][y] == 1

    def neighbors(self, x, y):
        """Return valid grid neighbors."""
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        valid = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if not self.is_obstacle(nx, ny):
                    valid.append((nx, ny))
        return valid