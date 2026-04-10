from src.planning.grid_map import GridMap
from src.planning.astar import AStarPlanner

m = GridMap()
m.random_obstacles(50)

a = AStarPlanner(m)
path = a.plan()

print(path)