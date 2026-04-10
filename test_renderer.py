from src.simulation.environment import Environment
from src.simulation.renderer import Renderer
import pygame, time

env = Environment()
renderer = Renderer(env)

for i in range(200):
    renderer.render()
    time.sleep(0.05)