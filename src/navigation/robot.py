# ============================
# robot.py
# Robot class & state
# ============================

class Robot:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.path = []
        self.path_index = 0

    def update_path(self, path):
        self.path = path
        self.path_index = 0

    def move_step(self):
        """Move 1 cell along planned path."""
        if self.path_index < len(self.path):
            self.x, self.y = self.path[self.path_index]
            self.path_index += 1

    def at_goal(self, goal):
        return (self.x, self.y) == goal