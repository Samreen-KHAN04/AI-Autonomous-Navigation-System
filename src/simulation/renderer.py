# ======================================
# renderer.py
# Draws simulation using Pygame
# ======================================

import pygame
from src.utils.config import *

class Renderer:
    def __init__(self, env):
        pygame.init()
        self.env = env
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AI Autonomous Navigation System")

    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(self.window, COLOR_GRID, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.window, COLOR_GRID, (0, y), (WINDOW_WIDTH, y))

    def draw_obstacles(self):
        for x in range(self.env.map.width):
            for y in range(self.env.map.height):
                if self.env.map.grid[x][y] == 1:
                    pygame.draw.rect(
                        self.window,
                        COLOR_OBSTACLE,
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    )

    def draw_path(self):
        for (x, y) in self.env.path:
            pygame.draw.rect(
                self.window,
                COLOR_PATH,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    def draw_robot(self):
        x, y = self.env.robot.x, self.env.robot.y
        pygame.draw.rect(
            self.window,
            COLOR_ROBOT,
            (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

    def draw_start_goal(self):
        sx, sy = self.env.map.start
        gx, gy = self.env.map.goal
        pygame.draw.rect(self.window, COLOR_START, (sx * CELL_SIZE, sy * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.window, COLOR_GOAL, (gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def render(self):
        self.window.fill(COLOR_BG)
        self.draw_grid()
        self.draw_obstacles()
        self.draw_path()
        self.draw_robot()
        self.draw_start_goal()
        pygame.display.update()