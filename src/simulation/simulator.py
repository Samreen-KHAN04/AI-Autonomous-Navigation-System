# ======================================
# simulator.py
# Runs simulation loop
# ======================================

import pygame
from src.navigation.controller import Controller

class Simulator:
    def __init__(self, env, renderer):
        self.env = env
        self.renderer = renderer
        self.controller = Controller(env.robot)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.env.robot.at_goal(self.env.map.goal):
                self.controller.step()

            self.renderer.render()
            clock.tick(10)  # 10 FPS

        pygame.quit()