# ======================================
# environment.py
# Holds environment + robot + map state
# ======================================

from src.planning.grid_map import GridMap
from src.navigation.robot import Robot

class Environment:
    def __init__(self):
        self.map = GridMap()
        self.map.random_obstacles(count=55)

        sx, sy = self.map.start
        self.robot = Robot(sx, sy)

        self.path = []

    def set_path(self, path):
        self.path = path
        self.robot.update_path(path)