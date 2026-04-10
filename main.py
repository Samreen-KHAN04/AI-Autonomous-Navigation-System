# ===========================
# main.py
# Execute the full project
# ===========================

from src.simulation.environment import Environment
from src.simulation.renderer import Renderer
from src.simulation.simulator import Simulator
from src.planning.astar import AStarPlanner

def main():
    # Create environment
    env = Environment()

    # Compute path
    planner = AStarPlanner(env.map)
    path = planner.plan()

    print("Generated Path:", path)
    env.set_path(path)

    # Visualization setup
    renderer = Renderer(env)
    simulator = Simulator(env, renderer)

    # Run simulation
    simulator.run()

if __name__ == "__main__":
    main()