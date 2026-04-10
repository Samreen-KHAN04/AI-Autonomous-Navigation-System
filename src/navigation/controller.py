# ================================
# controller.py
# Control movement of robot
# ================================

class Controller:
    def __init__(self, robot):
        self.robot = robot

    def step(self):
        """Robot performs one movement update."""
        self.robot.move_step()