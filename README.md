🚗 AI-Based Autonomous Navigation System  
### Virtual Robot Navigation using Python, OpenCV, Pygame & A* Path Planning

---

## 📌 Overview
This project implements a complete **AI-based autonomous navigation system** inside a **virtual 2D simulation environment**.

A virtual robot:
- Perceives the surroundings  
- Detects obstacles  
- Computes an optimal path using **A\***  
- Navigates autonomously from start → goal  
- Avoids obstacles  
- Displays real-time movement in Pygame  

This project is designed as a **portfolio-ready GitHub project** ideal for placements, internships, and academic submissions.

---

## 🎯 Problem Statement
**“How can a robot autonomously navigate from a start point to a destination while avoiding obstacles without human control?”**

This system solves the problem through:
- Simulated perception  
- Obstacle detection  
- Optimal path planning  
- Navigation & control  
- Real-time 2D visualization  

---

## 🚀 Features
- Virtual robot agent  
- Random obstacle generation  
- Grid-based environment (2D map)  
- A\* optimal path planning  
- Smooth robot navigation  
- Real-time simulation using Pygame  
- Modular and scalable codebase  
- Beginner-friendly and hardware-independent  

---

## 🧠 Tech Stack

| Component       | Technology |
|----------------|------------|
| Language       | Python 3.10 |
| Vision (mock)  | OpenCV, NumPy |
| Planning       | A\* Algorithm |
| Simulation     | Pygame |
| Math & Arrays  | NumPy |
| Visualization  | Matplotlib, Pygame |
| Documentation  | Markdown |

---

## 🏗 Project Architecture


Perception → Obstacle Map → A* Path Planning → Navigation Controller → Simulation Renderer


### 📦 **Block Diagram**


+---------------------------+
| Grid Map |
+-------------+-------------+
|
v
+---------------------------+
| Perception Module |
+---------------------------+
|
v
+---------------------------+
| Obstacle Detection |
+---------------------------+
|
v
+---------------------------+
| A* Path Planning |
+---------------------------+
|
v
+---------------------------+
| Navigation & Simulation |
+---------------------------+


---

## 📁 Folder Structure

### **Current Structure**
```
AI-Autonomous-Navigation-System/
│
├── src/
│   ├── perception/
│   │   ├── camera_simulator.py
│   │   ├── lane_detection.py
│   │   └── obstacle_detection.py
│   ├── planning/
│   │   ├── astar.py
│   │   └── grid_map.py
│   ├── navigation/
│   │   ├── controller.py
│   │   └── robot.py
│   ├── simulation/
│   │   ├── environment.py
│   │   ├── renderer.py
│   │   └── simulator.py
│   └── utils/
│       ├── config.py
│       ├── helpers.py
│       └── logger.py
│
├── data/
│   └── maps/
│       └── sample_frames/
│
├── main.py
├── requirements.txt
├── test_astar.py
├── test_renderer.py
└── README.md
```

### **Planned Structure (Future)**
```
├── outputs/
│   ├── screenshots/
│   ├── simulation_videos/
│   └── generated_paths/
│
├── notebooks/
├── docs/
├── images/
└── videos/
```


---

## 🛠 Installation

```bash
git clone https://github.com/Samreen-KHAN04/AI-Autonomous-Navigation-System
cd AI-Autonomous-Navigation-System

# Create a virtual environment

Windows

python -m venv nav-env
nav-env\Scripts\activate

Mac/Linux

python3 -m venv nav-env
source nav-env/bin/activate
Install dependencies
pip install -r requirements.txt
▶️ Run the Simulation
python main.py
Expected Output
Grid world appears
Red blocks = obstacles
Blue = start point
Yellow = goal
Green = computed path (A*)
White box = robot moving along the path

🧩 Future Enhancements
Support real camera input
YOLO-based dynamic obstacle detection
Lane detection module
Reinforcement Learning–based navigation (DQN / PPO)
ROS2 + Gazebo integration
3D path planning (RRT*, D*)
Multi-robot coordination
🏅 Learning Outcomes
Implementing A* path planning
Building AI simulations
Understanding grid-based navigation
Robotics control fundamentals
Python modular coding
Visualizations & animations
Working with Pygame & OpenCV
👩‍💻 Author

Samreen
AI & Robotics Enthusiast
B.Tech – IT Engineering

Built under guidance with Spark (AI assistant)